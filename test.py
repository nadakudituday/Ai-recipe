import base64
import requests
import streamlit as st
import os
from PIL import Image

# API Configuration
FLASK_SERVER_URL = "http://127.0.0.1:5000/latest_image"  # Flask backend for ESP32 images
API_KEY = "your api key"  # Replace with your actual API key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"

st.title("AI Recipe Predictor")

# Function to fetch the latest ESP32 image
def fetch_latest_image():
    try:
        response = requests.get(FLASK_SERVER_URL)
        if response.status_code == 200:
            return response.json().get("image_url")
    except Exception as e:
        st.error(f"Error fetching image: {e}")
    return None

# Function to encode local image to base64
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Function to encode image from a URL
def encode_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode("utf-8")
    except Exception as e:
        st.error(f"Error encoding image from URL: {e}")
    return None

# Select scenario
scenario = st.selectbox(
    "Select a Scenario",
    ("Diet-Friendly Recipes", "Ingredient-Based Recipes", "Quick Meals")
)

def ai_chemist_simulation(scenario):
    if scenario == "Diet-Friendly Recipes":
        return st.text_input("Enter dietary requirements:")
    elif scenario == "Ingredient-Based Recipes":
        return st.text_area("Enter main ingredients:")
    elif scenario == "Quick Meals":
        return st.text_input("Enter desired meal type:")
    return ""

target = ai_chemist_simulation(scenario)

# File uploader for images
uploaded_files = st.file_uploader("Upload food images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
image_paths = []
if uploaded_files:
    for img in uploaded_files:
        image = Image.open(img)
        image_path = f"temp_{img.name}"
        image.save(image_path, format="JPEG")
        image_paths.append(image_path)
        st.image(image, use_column_width=True)

# Function to fetch recipes
def fetch_recipes(prompt, image_paths):
    image_inputs = []
    for img in image_paths:
        if img.startswith("http"):  # Check if it's a URL
            encoded_image = encode_image_from_url(img)
        else:  # It's a local file
            encoded_image = encode_image(img)

        if encoded_image:
            image_inputs.append({"inlineData": {"mimeType": "image/jpeg", "data": encoded_image}})

    payload = {"contents": [{"role": "user", "parts": [{"text": prompt}] + image_inputs}], "generationConfig": {"maxOutputTokens": 2000, "temperature": 0.9, "topK": 40}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return [cand.get("content", {}).get("parts", [{}])[0].get("text", "No response") for cand in response.json().get("candidates", [])][:4]
    else:
        return [f"Error: {response.status_code} - {response.text}"]

# Get latest image from ESP32 and predict recipe
if st.button("Get Latest Image & Predict Recipe"):
    latest_image_url = fetch_latest_image()
    if latest_image_url:
        st.image(latest_image_url, caption="Latest Captured Image", use_column_width=True)
        prompt = "Generate 4 unique recipes using the ingredients detected in the image."
        if target:
            prompt += f" Also include these additional ingredients: {target}."
        recipes = fetch_recipes(prompt, [latest_image_url])
        for idx, recipe in enumerate(recipes, start=1):
            st.subheader(f"Recipe {idx}")
            st.write(recipe)
    else:
        st.error("No latest image available. Please capture an image using ESP32-CAM.")

# Generate recipes from uploaded images
if st.button("Predict Recipes from Images"):
    if image_paths:
        prompt = "Generate 4 unique recipes based on ingredients in the image."
        if target:
            prompt += f" Also include these additional ingredients: {target}."
        recipes = fetch_recipes(prompt, image_paths)
        for idx, recipe in enumerate(recipes, start=1):
            st.subheader(f"Recipe {idx}")
            st.write(recipe)
    else:
        st.error("No images provided! Please upload an image.")

# Generate recipes from manual input
if st.button("Predict Recipes from Ingredients"):
    if target:
        recipes = fetch_recipes(f"Generate 4 unique recipes using these ingredients: {target}.", [])
        for idx, recipe in enumerate(recipes, start=1):
            st.subheader(f"Recipe {idx}")
            st.write(recipe)
    else:
        st.error("Please enter ingredients first.")

