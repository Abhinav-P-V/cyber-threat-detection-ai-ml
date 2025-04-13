# Cyber Threat Detection Using AI & ML 🔐🤖

This project detects malicious insider threats using machine learning techniques like Isolation Forests and visualizes results in real-time through a Streamlit dashboard.

## 👨‍💻 Team Members
- Abhinav P V – ML & Backend
- Abhinav Gadde – Data & Feature Engineering
- Indushree – Frontend & Deployment

## 📁 Project Structure
```
project/
├── data/              # Datasets (CERT or mock logs)
├── model/             # Training scripts, ML model
├── backend/           # Flask API
├── frontend/          # Streamlit dashboard
├── notebooks/         # EDA in Jupyter
```

## 🚀 How to Run

### 1. Train the Model
```bash
cd model
python train_model.py
```

### 2. Start Flask Backend
```bash
cd backend
python app.py
```

### 3. Launch Streamlit Dashboard
```bash
cd frontend
streamlit run streamlit_app.py
```

## 🧠 Features
- Real-time anomaly detection
- Behavioral analysis using logs
- Flask + Streamlit integration
