import os
from data_generator import generate_retail_data
from elasticity_model import train_demand_model
from optimizer import find_optimal_price

def run_pricing_pipeline():
    data_path = "../data/simulated_sales.csv"
    base_price = 100.0
    
    # 1. Generate Data (Simulating a database pull)
    df = generate_retail_data(data_path)
    
    # 2. Train the Elasticity Model
    model = train_demand_model(df)
    
    # 3. Run the Financial Optimizer
    # We constrain the optimizer: we won't price it below €40 or above the €100 base price
    opt_price, exp_demand, max_rev = find_optimal_price(model, min_price=40.0, max_price=base_price)
    
    optimal_discount = ((base_price - opt_price) / base_price) * 100
    
    print("\n================ BUSINESS DECISION OUTPUT ================")
    print(f"Original Price:          €{base_price:.2f}")
    print(f"Algorithm Optimal Price: €{opt_price:.2f}")
    print(f"Recommended Markdown:    {optimal_discount:.1f}%")
    print(f"Expected Sales Volume:   {int(exp_demand)} units")
    print(f"Projected Max Revenue:   €{max_rev:.2f}")
    print("==========================================================")

if __name__ == "__main__":
    run_pricing_pipeline()
