import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


def machine_learning():
    data = pd.read_csv(r'.\resources\datasets\customers.csv')
    #dataset (create pending)
    print(data.head())

    #fill missing values
    data.ffill(inplace=True)

    data['Subscription_Type'] = data['Subscription_Type'].map({
        'Basic': 0,
        'Standard': 1,
        'Premium': 2
    })
    # Features and target
    X= data[['Age', 'Subscription_Type', 'Usage']]
    y = data['Churn']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

    #Initialize Randon Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train Model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    #Evaluations
    accuracy = accuracy_score(y_test, y_pred)
    print(f'accuracy: {accuracy*100:.2f}%')

    feature_importance = model.feature_importances_
    features = X.columns
    plt.bar(features, feature_importance)
    plt.title('Feature Importance')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.show()
