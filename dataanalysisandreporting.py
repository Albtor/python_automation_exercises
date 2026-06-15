import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#pip install pandas, matplotlib seaborn

def data_analysis_and_reporting():
    data = pd.read_csv("resources/datasets/finantial_data.csv")
    print(data.head())

    total_revenue = data["Revenue"].sum
    total_expenses = data["Expenses"].sum
    total_profit = data["Profit"].sum

    print("Total revenue:", total_revenue)
    print("Total Expenses:", total_expenses)
    print("Total Profit:", total_profit)

    sns.set_style("whitegrid")
    plt.figure(figsize=(10,6))
    plt.plot(data['Month'], data['Revenue'], label="Revenue", marker='o', color='b')