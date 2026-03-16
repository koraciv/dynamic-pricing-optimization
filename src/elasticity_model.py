from sklearn.linear_model import LinearRegression
import numpy as np

def train_demand_model(df):
    print("Training Price Elasticity Regression Model...")
    
    # Features (X) and Target (y)
    # We use actual_price to predict sales_volume
    X = df[['actual_price']].values
    y = df['sales_volume'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # The coefficient tells us exactly how many sales we lose for every €1 increase
    price_sensitivity = model.coef_[0]
    
    print(f"Model trained. Estimated Price Sensitivity: {price_sensitivity:.2f} units per €1")
    return model
