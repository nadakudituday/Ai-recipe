# AI Recipe Predictor

## 🚀 Project Overview
AI Recipe Predictor is a  Streamlit-based web application that generates personalized recipes using AI. Users can input ingredients manually or upload images to get recipe suggestions powered by the Google Gemini API.


## 🎯 Features

### 🔹 Scenario-Based Recipe Generation
- 🥗 Diet-Friendly Recipes – Based on dietary preferences (e.g., keto, vegan)
- 🍅 Ingredient-Based Recipes – Enter available ingredients for recipe ideas
- ⏳ Quick Meals – Get recipes under 30 minutes

### 🔹 Image-Based Recipe Prediction
- 📸 Upload food images (supports JPG, PNG)
- 🔄 Fetch latest images from **ESP32-CAM** (via Flask API)

### 🔹 AI-Powered Recipe Generation
- 📜 Step-by-step cooking instructions
- 🕒 Estimated cooking time
- 🍽️ Serving suggestions

### 🔹 User-Friendly Interface
- 🔼 Upload images or enter text
- 🎛️ Customizable dietary constraints
- ⚡ Fast and interactive


## 🏗️ Tech Stack
- Frontend: Streamlit 🖥️
- Backend: Flask (for ESP32 Image Processing) 🌍
- AI Model: Google Gemini API 🤖
- Cloud & API Integration: Requests, Base64 Encoding 🌐
- Image Processing: PIL (Pillow) 📷


## 📂 Project Structure
```
📂 AI-Recipe-Predictor
│── 📜 app.py              # Main Streamlit app
│── 📜 flask_server.py     # ESP32 Image Fetching API
│── 📂 images              # Uploaded & Captured Images
│── 📂 templates           # Frontend assets (if needed)
│── 📜 requirements.txt    # Python dependencies
│── 📜 README.md           # Project documentation
```

---

## 🔧 Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AI-Recipe-Predictor.git
cd AI-Recipe-Predictor
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Flask Server (For ESP32 Image Fetching)
```bash
python flask_server.py
```

### 4️⃣ Run Streamlit App
```bash
streamlit run app.py
```

---

## 📌 Next Steps & Enhancements
✅ Improve UI with Custom Styling  
✅ Add More AI Model Variants (OpenAI GPT, Bard)  
✅ Integrate a Database for Recipe Storage 
✅ Deploy on Streamlit Cloud / AWS / Heroku  

---

## 📝 Contribute & GitHub Setup
🌟 Fork the Repository  
📌 Create a Branch: `git checkout -b feature-new`  
✅ Commit Changes: `git commit -m "Added feature XYZ"`  
🚀 Push to GitHub: `git push origin feature-new`  
🔄 Create a Pull Request (PR) 

📌 GitHub Repository Link: [🔗 Your GitHub Repo](https://github.com/your-username/AI-Recipe-Predictor)  

---

### 💡 Have Suggestions?
Feel free to open an issue or submit a pull request! 😊


![pro1](https://github.com/user-attachments/assets/aabd57a6-8f3c-4701-b290-67c7c7420331)
![pro2](https://github.com/user-attachments/assets/304e2275-343c-4696-9510-9ae61397cc7a)
