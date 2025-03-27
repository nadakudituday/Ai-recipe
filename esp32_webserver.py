from flask import Flask, render_template, Response, jsonify
import cv2
import threading
import requests
import numpy as np
import time
import os

app = Flask(__name__)

ESP32_URL = "http://192.168.131.229:81/stream"  # Update with ESP32-CAM IP
IMGBB_API_KEY = "dcc0178a24b1804b5f1b37d1ca01abe8"  # Replace with your ImgBB API key
latest_image_url = None  # Store latest uploaded image URL

# Global frame storage
frame = None
lock = threading.Lock()

def fetch_stream():
    """ Continuously fetch frames from ESP32 and store in a global variable """
    global frame
    while True:
        try:
            img_resp = requests.get(ESP32_URL, stream=True, timeout=5)
            if img_resp.status_code == 200:
                bytes_data = b""
                for chunk in img_resp.iter_content(chunk_size=1024):
                    bytes_data += chunk
                    a = bytes_data.find(b'\xff\xd8')
                    b = bytes_data.find(b'\xff\xd9')
                    if a != -1 and b != -1:
                        jpg = bytes_data[a:b+2]
                        bytes_data = bytes_data[b+2:]
                        temp_frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        with lock:
                            frame = temp_frame
        except Exception as e:
            print(f"Error fetching stream: {e}")

# Start the stream in a separate thread
threading.Thread(target=fetch_stream, daemon=True).start()

def generate_frames():
    """ Serve frames stored in global variable to multiple clients """
    while True:
        with lock:
            if frame is None:
                continue
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    """ Capture the latest frame and upload it to ImgBB """
    global latest_image_url
    with lock:
        if frame is not None:
            filename = f"captured_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            img_url = upload_to_imgbb(filename)
            latest_image_url = img_url
            return jsonify({"message": "Image captured and uploaded", "image_url": img_url})
    return jsonify({"message": "No frame available"})

@app.route('/latest_image')
def latest_image():
    """ Return the latest captured image URL """
    if latest_image_url:
        return jsonify({"image_url": latest_image_url})
    return jsonify({"message": "No image available"})

def upload_to_imgbb(img_path):
    """ Uploads the captured image to ImgBB and returns the image URL """
    with open(img_path, "rb") as file:
        response = requests.post(
            "https://api.imgbb.com/1/upload",
            params={"key": IMGBB_API_KEY},
            files={"image": file},
        )
    if response.status_code == 200:
        image_url = response.json()["data"]["url"]
        print(f"Uploaded Image URL: {image_url}")
        return image_url
    else:
        print("Failed to upload image")
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
