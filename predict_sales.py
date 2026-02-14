import pandas as pd
import pickle
import numpy as np
from datetime import datetime

def run_prediction():
    # Load model and encoders
    try:
        with open('sales_model_xgb.pkl', 'rb') as f:
            artifacts = pickle.load(f)
    except FileNotFoundError:
        print("\n[ERROR] 'sales_model_xgb.pkl' not found. Please run the training script first.")
        return

    model = artifacts['model']
    prod_enc = artifacts['prod_enc']
    store_enc = artifacts['store_enc']
    
    # Create lowercase mappings for case-insensitive input
    prod_map = {p.lower(): p for p in prod_enc.classes_}
    store_map = {s.lower(): s for s in store_enc.classes_}

    print("\n" + "="*45)
    print("      GROCERY SALES PREDICTION SYSTEM      ")
    print("="*45)
    
    # Input Product with case-insensitivity
    user_prod = input(f"Enter Product Name: ").strip().lower()
    if user_prod not in prod_map:
        print(f"\n[!] Product '{user_prod}' not recognized.")
        print(f"Available: {', '.join(prod_enc.classes_)}")
        return
    product = prod_map[user_prod]

    # Input Store with case-insensitivity
    user_store = input(f"Enter Store Name: ").strip().lower()
    if user_store not in store_map:
        print(f"\n[!] Store '{user_store}' not recognized.")
        print(f"Available: {', '.join(store_enc.classes_)}")
        return
    store = store_map[user_store]

    # Input Date
    date_str = input("Enter Date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    try:
        if not date_str:
            date_obj = datetime.now()
        else:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("\n[!] Invalid date format. Please use YYYY-MM-DD.")
        return

    # Prepare features (using 0/defaults for dynamic features like lags in this simple demo)
    input_features = pd.DataFrame([{
        'product_enc': prod_enc.transform([product])[0],
        'store_enc': store_enc.transform([store])[0],
        'aisle_enc': 0, 
        'unit_price': 10.0, 
        'day_of_week': date_obj.weekday(),
        'month': date_obj.month,
        'day': date_obj.day,
        'lag_1': 0, 'lag_7': 0, 'lag_30': 0,
        'roll_mean_7': 0, 'roll_mean_30': 0
    }])

    # Ensure column order matches training
    X_input = input_features[artifacts['feature_cols']]
    
    # Predict
    prediction = model.predict(X_input)[0]
    final_val = max(0, prediction)

    # Prettier Output
    print("\n" + "-"*45)
    print(f" RESULTS FOR: {product} @ {store}")
    print(f" DATE:        {date_obj.strftime('%A, %B %d, %Y')}")
    print("-"*45)
    print(f" PREDICTED SALES QUANTITY: {final_val:.2f} units")
    print("="*45 + "\n")

if __name__ == "__main__":
    run_prediction()