import pandas as pd

def data_engineering():
    data = pd.read_csv("./customers.csv") #check
    print(data.head())
    data_clean = data.dropna()
    data_clean = data_clean[data_clean['Age']>=30]
    print(data_clean.head())


# pip install pandas sqlalchemy sqlite3
# .venv312\Scripts\activate