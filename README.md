# 🩺 MediMitra AI

**MediMitra** is an AI-powered health assistant that analyzes user symptoms, predicts possible diseases using machine learning, evaluates severity, and suggests nearby hospitals if required.

---

## 🚀 Features

* 🧠 Symptom-based disease prediction
* ⚠️ Severity detection (Serious / Not Serious)
* 🏥 Nearby hospital recommendation
* 📝 OCR support (extract text from reports/images)
* 🌐 Clean and interactive web interface

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS (Glassmorphism UI)
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (Naive Bayes / Logistic Regression)
* **Other Modules:** OCR, Rule-based decision engine

---

## 📂 Project Structure

MediMitra/
│
├── app.py
├── config.py
├── models/
│   ├── heart.pkl
│   ├── asthma.pkl
│   ├── cancer.pkl
│   └── abdominal.pkl
│
├── modules/
│   ├── classifier.py
│   ├── decision_engine.py
│   ├── llm_handler.py
│   └── ocr_server.py
│
├── utils/
│   └── hospital_finder.py
│
├── data/
│   └── hospital_data.json
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

---

## ⚙️ How to Run

### 1. Clone Repository

git clone https://github.com/your-username/MediMitra-AI.git

### 2. Go to Project Folder

cd MediMitra-AI

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run App

python app.py

### 5. Open Browser

http://127.0.0.1:5000/

---

## 🧪 Example Input

I have chest pain and shortness of breath

### Output:

<img width="1406" height="858" alt="image" src="https://github.com/user-attachments/assets/3dce531c-e73c-4eeb-9001-7452d9b6fa7e" />

---

## 📌 Future Improvements

* 🔊 Voice input integration
* 📍 Real-time hospital API (Google Maps)
* 📄 Upload medical reports (OCR enhancement)
* 🤖 Advanced deep learning models

---

## ⚠️ Disclaimer

This project is for educational purposes only and should not be used as a replacement for professional medical advice.

---

## 👩‍💻 Author

**Anamika Negi**
AI Enthusiast

---
