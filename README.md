# Sales Prediction System for Grocery Stores

A machine learning system to predict next-day sales for grocery products, helping retailers reduce stock issues.

## 📁 Files Included

1. **sales_prediction_fixed.ipynb** - Jupyter notebook for training the model
2. **predict_sales.py** - Terminal script for making predictions
3. **grocery_chain_data.csv** - Your sales dataset (1980+ transactions)
4. **README.md** - This file

## 🚀 Quick Start

### Step 1: Train the Model

Open the Jupyter notebook in VS Code or Jupyter:

```bash
# If using Jupyter
jupyter notebook sales_prediction_fixed.ipynb

# If using VS Code
# Just open the .ipynb file in VS Code
```

Run all cells in the notebook. This will:
- Load and analyze your data
- Create time-series features
- Train 4 different models
- Save the best model as `sales_prediction_model.pkl`

**Expected Training Time:** 2-5 minutes

### Step 2: Make Predictions

Once the model is trained, use the terminal script:

#### Interactive Mode (Easiest)
```bash
python predict_sales.py
```

The script will guide you through:
1. Selecting a product
2. Selecting a store
3. Entering a prediction date (or use tomorrow by default)

#### Command Line Mode
```bash
# Predict sales for Milk at GreenGrocer Plaza (tomorrow)
python predict_sales.py --product "Milk" --store "GreenGrocer Plaza"

# Predict for a specific date
python predict_sales.py --product "Bread" --store "ValuePlus Market" --date "2025-05-15"

# List all available products
python predict_sales.py --list-products

# List all available stores
python predict_sales.py --list-stores
```

## 📊 Understanding the Output

When you run a prediction, you'll see:

```
============================================================
SALES PREDICTION
============================================================
Product: Milk
Store: GreenGrocer Plaza
Prediction Date: 2025-05-15 (Thursday)
============================================================

📊 PREDICTION RESULTS:
   Predicted Sales: 12.3 units

📈 Recent Sales History (last 7 days):
   2025-05-14: 10 units
   2025-05-13: 15 units
   2025-05-12: 8 units
   ...

   Average (7-day): 11.2 units
   Prediction vs Avg: +9.8%

💡 STOCK RECOMMENDATION:
   Minimum Stock: 13 units
   Recommended Stock (with 20% buffer): 15 units
```

## 🎯 Model Performance

The system trains 4 models and automatically selects the best one:
- Linear Regression (baseline)
- Ridge Regression (regularized)
- **Random Forest** (usually best)
- Gradient Boosting

Typical performance metrics:
- **MAE (Mean Absolute Error):** ~1-2 units
- **R² Score:** 0.7-0.8 (70-80% variance explained)
- **MAPE:** 15-25% (average prediction error)

## 🔑 Key Features Used

The model uses these factors to predict sales:

1. **Historical Sales Patterns:**
   - Yesterday's sales (most important)
   - Sales from 2, 3, 7, and 14 days ago
   - Rolling averages (3, 7, 14 days)

2. **Time-Based Features:**
   - Day of week (Monday-Sunday)
   - Is it a weekend?
   - Month and season
   - Beginning/end of month

3. **Product Information:**
   - Product category/aisle
   - Store location

## 📝 Common Use Cases

### 1. Daily Stock Planning
```bash
# Run every morning to get next-day predictions for all key products
python predict_sales.py --product "Milk" --store "GreenGrocer Plaza"
python predict_sales.py --product "Bread" --store "GreenGrocer Plaza"
python predict_sales.py --product "Eggs" --store "GreenGrocer Plaza"
```

### 2. Weekend Preparation
```bash
# Check Friday predictions for weekend stock
python predict_sales.py --product "Milk" --store "GreenGrocer Plaza" --date "2025-05-16"
python predict_sales.py --product "Milk" --store "GreenGrocer Plaza" --date "2025-05-17"
```

### 3. New Store Opening
The model works best when you have at least 2 weeks of sales history for a product-store combination.

## ⚙️ Requirements

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

All requirements are in the notebook and will be installed automatically when you run it.

## 🔄 Updating the Model

**Retrain Monthly** with new data:

1. Add new sales transactions to `grocery_chain_data.csv`
2. Re-run the Jupyter notebook
3. The new model will automatically replace the old one

## 📈 Tips for Better Predictions

1. **More History = Better Predictions**
   - At least 14 days of history per product recommended
   - 30+ days is ideal

2. **Consistent Data Entry**
   - Record sales daily
   - Use consistent product names
   - Don't skip days

3. **Monitor Accuracy**
   - Compare predictions vs actual sales
   - Identify products with high errors
   - Consider manual adjustments for those

4. **Special Events**
   - The current model ignores promotions
   - Manually adjust predictions during sales/holidays
   - Future versions can include promotion flags

## 🛠️ Troubleshooting

### Error: "Model file not found"
**Solution:** Run the Jupyter notebook first to train the model.

### Error: "Product not in training data"
**Solution:** 
- Check spelling (product names are case-sensitive)
- Use `--list-products` to see available products
- Train model with new product data

### Error: "No sales history found"
**Solution:** This product-store combination needs at least 1 day of sales history.

### Poor Predictions for a Product
**Possible causes:**
- Product has irregular sales patterns
- Not enough historical data
- Product affected by external factors (weather, events)

## 📞 Support

For questions or issues:
1. Check this README
2. Review the notebook comments
3. Examine the prediction script help: `python predict_sales.py --help`

## 📄 License

This is a custom sales prediction system. Use and modify as needed for your business.

---

**Created:** 2025
**Last Updated:** 2025
**Version:** 1.0
