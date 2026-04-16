```markdown
# Credit Card Fraud Detection Microservice 🚀

## Overview
This is a production-grade REST API designed for real-time Credit Card Fraud Detection. The system utilizes a highly-tuned **XGBoost Classifier** optimized through **Optuna (Bayesian Optimization)**. It is specifically engineered to handle extreme class imbalance and provide reliable predictions in a high-stakes financial environment.

The microservice is fully containerized using **Docker** and served via **FastAPI**, ensuring high-performance asynchronous inference and environment consistency.

## Key Features
* **Algorithm:** Optimized XGBoost (Sniper Mode).
* **Optimization:** Hyperparameter tuning via Optuna for maximum AUPRC.
* **Architecture:** Dockerized for seamless deployment and dependency isolation.
* **Performance:** Asynchronous FastAPI implementation for low-latency requests.
* **Preprocessing:** Integrated `RobustScaler` to manage extreme transaction outliers.

## Model Performance (Final Test Set)
* **Precision:** 90% (Strictly controlled to minimize customer friction).
* **AUPRC:** 0.881 (Area Under Precision-Recall Curve - Exceptional for highly imbalanced data).
* **Recall:** 82.7% (Effective capture rate of fraudulent activities).
* **False Positives:** Only 9 out of 56,864 genuine transactions were incorrectly flagged.

## Tech Stack
* Python 3.11
* XGBoost
* Scikit-Learn
* FastAPI / Uvicorn
* Docker
* Joblib / JSON Serialization

## Project Structure
```text
fraud_detection_project/
├── app/
│   ├── main.py          # FastAPI Entry Point & Pydantic Models
│   └── model_utils.py   # Inference Logic & Data Re-ordering
├── models/              # Serialized Model Artifacts
│   ├── robust_scaler.joblib
│   └── fraud_model_xgboost.json
├── tests/               # Automated Unit & API Tests
│   └── test_api.py
├── Dockerfile           # Containerization Script
└── requirements.txt     # Environment Dependencies
```

## Getting Started

### Prerequisites
* **Docker Desktop** must be installed and running on your host machine.

### Run with Docker (Recommended)
1.  **Build the Image:**
    ```bash
    docker build -t credit-fraud-app .
    ```
2.  **Run the Container:**
    ```bash
    docker run -p 8000:8000 credit-fraud-app
    ```
3.  **Interactive API Docs:**
    Navigate to `http://localhost:8000/docs` to access the interactive Swagger UI for live testing.

### Manual Setup (Virtual Environment)
1.  Create environment: `python -m venv venv`
2.  Activate: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
3.  Install dependencies: `pip install -r requirements.txt`
4.  Start server: `uvicorn app.main:app --reload`

## API Endpoints
* **GET /**: Health check and microservice status.
* **POST /predict**: Accepts a JSON payload containing transaction features (V1-V28, Time, Amount). It returns the fraud probability, a Boolean flag, and a business recommendation (ALLOW/BLOCK).

---
**Developed by:** Lead AI/ML Engineer  
**Status:** Production Ready ✅
```
```