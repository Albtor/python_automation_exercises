import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv(r'.\resources\datasets\customers.csv')
#dataset (create pending)
print(data.head())

#fill missing values
data.fillna(method='ffill',inpalce=True)

data['Subscription_Type'] = data['Subscription_Type'].map({'Basic':0, 'Premium':1})
