# Sales Prediction System for Grocery Stores


🚀 Getting Started
1. Install Dependencies:
pip install pandas numpy xgboost scikit-learn
2. Prepare Your Data:
Ensure grocery_chain_data.csv is in the root folder.
3. Train the Model:
python train_model.py
4. Predict Sales:
python predict_sales.py
🛠️ How It Works
The system processes historical transaction data to create time-based features (lags, rolling means, and calendar effects) to forecast demand. The interactive script is case-insensitive, meaning you can type 'apples' or 'Apples' and get the same accurate result.
📊 Model Details
•	Algorithm: XGBoost Regressor
•	Output: Predicted quantity (rounded to 2 decimal places)
•	Features: Product/Store encoding, seasonality, and historical sales trends.

