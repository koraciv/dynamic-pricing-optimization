from scipy.optimize import minimize_scalar

def objective_function(price, model):
    # Predict demand for this specific price
    predicted_demand = model.predict([[price]])[0]
    
    # Revenue = Price * Demand
    revenue = price * predicted_demand
    
    # Scipy's 'minimize' function looks for the lowest number. 
    # To maximize revenue, we tell it to minimize NEGATIVE revenue.
    return -revenue

def find_optimal_price(model, min_price, max_price):
    print(f"Running optimization algorithm between €{min_price} and €{max_price}...")
    
    # minimize_scalar finds the local minimum of an equation
    result = minimize_scalar(
        objective_function, 
        bounds=(min_price, max_price), 
        args=(model,), 
        method='bounded'
    )
    
    optimal_price = result.x
    expected_demand = model.predict([[optimal_price]])[0]
    max_revenue = optimal_price * expected_demand
    
    return optimal_price, expected_demand, max_revenue
