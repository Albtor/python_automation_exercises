import tensorflow as tf
import mlflow
import mlflow.keras
import tensorflow.keras
import layers, models
from sklearn.model_selection import train_test_split
# py -3.12 -m venv .venv312
# .venv312\Scripts\activate
# pip install tensorflow


def ml_workflows():
    # Load fashin MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    # Normalize pixel values to be between 0 and 1
    x_train, x_test = x_train / 255.0, x_test / 255.0
    # Reshape data to fit input shape of the model (28x28x1)
    x_train = x_train.reshape(-1,28,28,1)
    x_test = x_test.reshape(-1,28,28,1)

    # Build and Train Model
    # Define CNN model
    model = models.Sequential([layers.Conv2D(32,(3,3), activatin='relu', input_shape=(28,28,1)),
        layers.MaxPooling2D((2, 2))
        layers.Conv2D(64,(3,3), activaion='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64,(3,3), activaion='relu'),
        layers.Flatten(),
        layers.Dense(64,activation='relu'),
        layers.Dense(10, activation="softmax")
        ])
