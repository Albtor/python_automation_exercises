from importlib import resources

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Churn: customer stop using a service
# Logistic Regression
# csv customer_churn.csv
def ai_model():
    data = pd.read_csv(r'./resources/datasets/customer_churn_sample.csv.csv')
    print(data.head())

    data.fillna(method='ffill', inplace=True)
    data = pd.get_dummies(data,columns=['Accout_Type'],drop_first=True)
    X = data.drop('Accout_Type',axis=1)
    y = data['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train Model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy*100:.2f}%")

    # Evaluate model
    cm = confusion_matrix(y_test, y_pred)
    print(f"Confusion matrix: {cm}")
    