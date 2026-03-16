# Dynamic Pricing & Markdown Optimization

## 📌 Project Overview
In retail commerce, determining the correct discount for seasonal or clearance items is critical. A discount that is too deep sacrifices gross margin, while a discount that is too shallow results in unsold inventory and increased holding costs.

This project implements a **Financial Decision Model** to mathematically optimize retail markdowns. It utilizes machine learning to estimate the Price Elasticity of Demand and applies scientific optimization algorithms to calculate the exact price point that maximizes total revenue.

**Business Value:** Transitions pricing strategies from "gut feeling" rules to automated, data-driven financial decisions, directly impacting bottom-line profitability for e-commerce platforms.

## 🛠️ Tech Stack
* **Machine Learning:** scikit-learn (Linear Regression for Elasticity Modeling)
* **Mathematical Optimization:** SciPy (`minimize_scalar` for Revenue Maximization)
* **Data Engineering:** Pandas, NumPy
* **Language:** Python 3.x

## 🏗️ Architecture & Workflow
1. **Data Simulation:** Generates synthetic retail transaction data, modeling base demand, price sensitivity, and market noise to replicate a real-world database extraction.
2. **Elasticity Modeling:** Trains a regression model to map the mathematical relationship between historical discount percentages and resulting sales volume.
3. **Revenue Optimization:** Defines an objective function (`Revenue = Price * Predicted Demand`) and utilizes SciPy's bounded optimization algorithms to find the global maximum within acceptable retail pricing guardrails.
4. **Decision Output:** Translates the mathematical optimum into actionable business metrics (Optimal Price, Recommended Markdown %, Projected Revenue).

## 📂 Project Structure
```text
├── data/                   # Data directory (Dataset excluded via .gitignore)
├── src/                    
│   ├── data_generator.py   # Simulates retail pricing and demand data
│   ├── elasticity_model.py # scikit-learn regression model
│   ├── optimizer.py        # SciPy revenue maximization logic
│   └── main.py             # Pipeline orchestrator
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and directories
└── README.md               # Project documentation
