import xgboost as xgb
import joblib
import pandas as pd
import os

class FraudModel:
    def __init__(self):
        # 🏆 Local paths (Make sure models/ folder me ye dono exact naam se hain)
        self.scaler_path = "models/robust_scaler.joblib"
        self.model_path = "models/fraud_model_xgboost_optimized.json"  # <-- UPDATED
        
        # Loading artifacts
        self.scaler = joblib.load(self.scaler_path)
        self.model = xgb.XGBClassifier()
        self.model.load_model(self.model_path)

    def predict(self, data_dict: dict):
        # 1. Convert dict to DataFrame
        df = pd.DataFrame([data_dict])
        
        # 2. Production Scaling
        # Naye schema me extra columns nahi banane. Seedha Time aur Amount ko overwrite karenge.
        df[['Time', 'Amount']] = self.scaler.transform(df[['Time', 'Amount']])
        
        # 3. Exact Column Ordering (Fixes Feature Names Mismatch)
        # Kaggle dataset ka original order: Time, V1 to V28, Amount
        v_cols = [f'V{i}' for i in range(1, 29)]
        final_feature_order = ['Time'] + v_cols + ['Amount']
        
        # Model ko wahi order do jis pe usne training ki thi
        df_final = df[final_feature_order]
        
        # 4. Model Inference
        # predict_proba returns [prob_class_0, prob_class_1]
        prob = self.model.predict_proba(df_final)[:, 1][0]
        
        return float(prob)