import numpy as np
import pandas as pd
from numpy.ma.extras import column_stack
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


def datapreprocessing():
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

    #Scaling Data
    #1 MinMax Scalling
    scalerMinMax = MinMaxScaler()
    # data_normalized = pd.DataFrame(scalerMinMax.fit_transform(data[numerical_columns]))
    #2 standarization
    scalerStandard = StandardScaler()
    # data_standarized = pd.DataFrame(scalerStandard.fit_transform(data[numerical_columns]))
    #3 Label Encoding
    label_encoder = LabelEncoder()
    data['category_encoded'] = label_encoder.fit_transform(data['category_column'])
    #4 one hot encoding
    data_encoded = pd.get_dummies(data, columns=['category_column'], drop_first=True)

    #SCALING EXAMPLE
    sales_data = pd.read_csv(r'.\resources\sales_data.csv')
    numerical_imputer = SimpleImputer(strategy='median')
    sales_data[['age','income','sales_value']] = numerical_imputer.fit_transform(sales_data[['age','income','sales_value']])
    categorial_imputer2 = SimpleImputer(strategy='most_frequent')
    sales_data[['product_type']] = categorical_imputer.fit_transform(sales_data[['product_type']])
    scaler = StandardScaler()
    sales_data[['age','income','sales_value']] = scaler.fit_transform(sales_data[['age','income','sales_value']])
    sales_data_encoded = pd.get_dummies(sales_data, columns=['product_type'], drop_first=True)

    # Encoding Categorical Data
    sales_data_encoded = pd.get_dummies(sales_data, columns=['product_type'], drop_first=True)

    # Final Processed data
    print(sales_data_encoded.head())





