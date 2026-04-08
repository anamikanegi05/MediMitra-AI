🏥 MediMitra – AI Health Assistant
🚀 Overview

MediMitra is an AI-powered health assistant that analyzes user symptoms and provides:

Possible disease predictions (with probability, not certainty)
Basic health suggestions
Alerts for severe conditions
Nearby hospital recommendations (for critical cases)

The goal is to create a smart, user-friendly healthcare assistant that gives quick guidance while encouraging professional medical consultation.

✨ Features
🧠 Symptom-based Prediction using ML models
📊 Probability-based Output (not absolute diagnosis)
⚠️ Critical Condition Detection (e.g., chest pain → emergency alert)
🏥 Nearby Hospital Suggestions (for severe cases)
💬 Simple & Clean UI (HTML, CSS, Flask)
🔐 Secure & Extendable Architecture
🛠️ Tech Stack
Frontend: HTML, CSS (Bootstrap optional)
Backend: Flask (Python)
Machine Learning:
Scikit-learn
Naive Bayes / NLP-based classification
Database: SQLite (chat.db)
Others:
Pickle (.pkl) for model storage
📂 Project Structure
MediMitra/
│── app.py
│── chat.db
│── model/
│    ├── heart_model.pkl
│    ├── asthma_model.pkl
│    ├── cancer_model.pkl
│    ├── abdominal_model.pkl
│── modules/
│    ├── classifier.py
│    ├── decision_engine.py
│    ├── llm_handler.py
│    ├── ocr_server.py
│── templates/
│    ├── index.html
│── static/
│    ├── css/
│── README.md
⚙️ How It Works
User enters symptoms (e.g., chest pain, headache)
Text is processed using NLP
ML model predicts possible disease
Decision engine:
Adds probability
Detects severity
Output:
Suggestion
Warning (if critical)
Hospital recommendation (if needed)
🧪 Example Output
Symptoms: Chest pain, left arm pain

Prediction: Heart-related issue
Probability: 82%

⚠️ Warning: This may be a serious condition.
👉 Please visit the nearest hospital immediately.

Suggestion:
- Avoid physical exertion
- Stay calm
- Seek medical attention
▶️ Installation & Setup
1. Clone the repo
git clone https://github.com/your-username/medimitra.git
cd medimitra
2. Install dependencies
pip install -r requirements.txt
3. Run the app
python app.py
4. Open in browser
http://127.0.0.1:5000/
⚠️ Disclaimer

This project is not a medical diagnosis tool.
It only provides basic guidance and suggestions.
Always consult a qualified doctor for serious conditions.

💡 Future Improvements
🔍 Better NLP model (BERT / LLM integration)
📍 Real-time hospital API integration
📱 Mobile app version
🧾 Medical history tracking
🤖 Chatbot with conversational AI
🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.
📜 License

This project is open-source and available under the MIT License.
