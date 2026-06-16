import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from io import StringIO
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
    plt.plot(data['Month'], data['Expenses'], label="Expenses", color='r')
    plt.plot(data['Month'], data['Profit'], label="Profit", color='g')

    plt.title('Financial Overview (Monthly)', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Amount (in USD)', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

    data.set_index('Month')[['Revenue', 'Expenses', 'Profit']].plot(kind='bar', figsize=(10,6))
    plt.title('Financial Breakdown', fontsize=14)
    plt.ylabel('Amount (in USD)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def pdf_reporting():
    data = pd.read_csv("resources/datasets/finantial_data.csv")
    with PdfPages('financial_data.pdf') as pdf:
        plt.figure(figsize=(10,6))
        plt.plot(data['Month'], data['Revenue'], label="Revenue", marker='o', color='b')
        plt.plot(data['Month'], data['Expenses'], label="Expenses", color='r')
        plt.plot(data['Month'], data['Profit'], label="Profit", color='g')
        plt.title('Financial Overview (Monthly)', fontsize=14)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Amount (in USD)', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend()

        pdf.savefig()
        plt.close()

        # Plot the bar
        data.set_index('Month')[['Revenue', 'Expenses', 'Profit']].plot(kind='bar', figsize=(10,6))
        plt.title('Financial Breakdown', fontsize=14)
        plt.ylabel('Amount (in USD)', fontsize=12)
        plt.xticks(rotation=45)
        pdf.savefig()
        plt.close()

        summary = StringIO()
        summary.write("Total Revenue: {total_revenue}\n")
        summary.write("Total Expenses: {total_expenses}\n")
        summary.write("Total Profit: {total_profit}\n")

        plt.figure(figsize=(8,6))
        plt.text(0.5,0.5, summary.getvalue(), ha='center', va='center', fontsize=12, fontweight='bold')
        plt.axis('off')
        pdf.savefig()
        plt.close()


