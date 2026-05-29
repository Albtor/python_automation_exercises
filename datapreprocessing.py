import numpy as np
import pandas as pd
from numpy.ma.extras import column_stack
from sklearn.impute import SimpleImputer


def datapreprocessoing(file_path):
    # Removing missing data
    file_path = r'.\resources\sales_data.csv'
    data = pd.read_csv(file_path)
    data_cleaned = data.dropna(axis=0) #axis 0 is for rows
    data_cleaned = data.dropna(axis=1) #axis 1 is for columns

    # imputation: filling in the missin values some calculated values, numerical or categorical data
    imputer = SimpleImputer(strategy='mean')
    data_cleaned = pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=['float64','int64'])))
    categorical_columns = data.select_dtypes(include=['object']).columns
    categorical_imputer = SimpleImputer(strategy='most_frequent')
    data_cleaned[categorical_columns] = categorical_imputer.fit_transform(data[categorical_columns])

