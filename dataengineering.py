import pandas as pd
from sqlalchemy import create_engine
import time

# pip install pandas sqlalchemy sqlite3

def data_engineering():
    data = pd.read_csv("./resources/datasets/customers2.csv") #check
    print(data.head())
    data_clean = data.dropna()
    data_clean = data_clean[data_clean['Age']>=30]
    print(data_clean.head())

    # Load data into database
    engine = create_engine('sqlite:///Resources/customers.db, echo=True')
    data_clean.to_sql('customers', con=engine, if_exists='replace', index=False)
    print("Data Succesfully loaded into the database")

    # Automate ETL Process
    while True:
        data= pd.read_csv("./resources/datasets/customers2.csv")
        data_clean = data.dropna()
        data_clean = data_clean[data_clean['Age']>=30]
        data_clean.to_sql('customers', con=engine, if_exists='replace', index=False)
        print("ETL process completed successfully")
        time.sleep(5)

