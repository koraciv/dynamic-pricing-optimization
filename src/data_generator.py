import pandas as pd
import numpy as np
import os

def generate_retail_data(file_path, num_records=500):
    print("Generating simulated retail pricing data...")
    np.random.seed(42)
    
    # Simulate an item with a base price of €100
    base_price = 100.0
    
    # Randomly applied discounts between 0% and 50%
    discounts = np.random.uniform(0.0, 0.50, num_records)
    actual_prices = base_price * (1 - discounts)
    
    # Simulate Demand: Demand goes down as price goes up (Linear elasticity)
    # Base demand is 500 units. For every €1 increase, demand drops by 4 units.
    base_demand = 500
    price_sensitivity = 4.0 
    
    # Add some random market noise
    noise = np.random.normal(0, 15, num_records)
    
    demands = base_demand - (price_sensitivity * actual_prices) + noise
    # Ensure demand doesn't drop below 0
    demands = np.maximum(demands, 0).astype(int)
    
    df = pd.DataFrame({
        'day': range(1, num_records + 1),
        'original_price': base_price,
        'discount_pct': discounts,
        'actual_price': actual_prices,
        'sales_volume': demands
    })
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"Data successfully saved to {file_path}")
    return df
