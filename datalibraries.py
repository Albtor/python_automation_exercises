import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
# pip install scikit-learn

# Create 2D NumPy Array
def numpy_test():
    array = np.array([[1,2,3],[4,5,6]])
    result = array + 10
    print(result)


def pandas_test():
    data = {'Name': ['John', "George", "Paul","Ringo"], 'Age':[25,30,35]}
    df = pd.DataFrame(data)
    filtered_data = df[df['Age']>2825]
    print(filtered_data)


def sklearn_test():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,)

    # train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # evaluate performance
    score = model.score(X_test, y_test)
    print(f"Accuracy: {score * 100:.2f}%")

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     numpy_test()
#     pandas_test()
#     sklearn_test()