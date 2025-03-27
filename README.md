🍽️ AI Recipe Predictor - Project Overview
🚀 Project Description
AI Recipe Predictor is a Streamlit-based web application that generates personalized recipes using:
✅ Ingredient-based input (manual or via image)
✅ Dietary preferences & constraints
✅ Quick meal suggestions
💡 The app uses Google Gemini API to generate recipes dynamically.

🎯 Key Features
🔹 Scenario-Based Recipe Generation: Choose from:

🥗 Diet-Friendly Recipes – Enter dietary preferences (e.g., keto, vegan)

🍅 Ingredient-Based Recipes – Enter available ingredients

⏳ Quick Meals – Get recipes under 30 minutes

🔹 Image-Based Recipe Prediction:

📸 Upload food images (supports multiple formats)

🔄 Fetch images from ESP32-CAM (via Flask API)

🔹 AI-Powered Recipe Generation:

📜 Step-by-step cooking instructions

🕒 Estimated cooking time

🍽️ Serving suggestions

🔹 User-Friendly Interface:

🔼 Upload images or enter text

🎛️ Customizable dietary constraints

⚡ Fast and interactive

🏗️ Tech Stack
🔹 Frontend: Streamlit 🖥️
🔹 Backend: Flask (for ESP32 Image Processing) 🌍
🔹 AI Model: Google Gemini API 🤖
🔹 Cloud & API Integration: Requests, Base64 Encoding 🌐
🔹 Image Processing: PIL (Pillow), OpenCV (optional) 📷

📂 Project Structure
📂 AI-Recipe-Predictor
│── 📜 app.py              # Main Streamlit app
│── 📜 flask_server.py     # ESP32 Image Fetching API
│── 📂 images              # Uploaded & Captured Images
│── 📂 templates           # Frontend assets (if needed)
│── 📜 requirements.txt    # Python dependencies
│── 📜 README.md           # Project documentation
🔧 Setup & Installation
1️⃣ Clone the Repository

git clone https://github.com/your-username/AI-Recipe-Predictor.git
cd AI-Recipe-Predictor
2️⃣ Install Dependencies

pip install -r requirements.txt
3️⃣ Run Flask Server (For ESP32 Image Fetching)

python flask_server.py
4️⃣ Run Streamlit App

streamlit run app.py
📌 ![pro1](https://github.com/user-attachments/assets/aabd57a6-8f3c-4701-b290-67c7c7420331)
Next Steps & Enhancements
✅ Improve ![pro2](https://github.com/user-attachments/assets/304e2275-343c-4696-9510-9ae61397cc7a)
UI with Custom Styling
✅ Add More AI Model Variants (OpenAI GPT, Bard)
✅ Integrate a Database for Recipe Storage
✅ Deploy on Streamlit Cloud / AWS / Heroku

