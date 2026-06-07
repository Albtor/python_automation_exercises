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
                               layers.MaxPooling2D((2, 2)),
                               layers.Conv2D(64,(3,3), activaion='relu'),
                               layers.MaxPooling2D((2, 2)),
                               layers.Conv2D(64,(3,3), activaion='relu'),
                               layers.Flatten(),
                               layers.Dense(64,activation='relu'),
                               layers.Dense(10, activation="softmax")
                               ])
    # Compile Model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    # Log the exeriment with MLflow
    with mlflow.start_run():
        mlflow.log_param("batch_size", 64)
        mlflow.log_param("epochs", 10)
        # Train model
        model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))
        # log model
        mlflow.keras.log_model(model, "fashion_mnist_model")
        # Evaluate model
        test_loss, test_acc = model.evaluate(x_test, y_test)
        mlflow.log_metric("test_accuracy", test_acc)
        print(f"Test accuracy:{test_acc}")


    # Automating model testing

    # Log different hyperparameters
    for batch_size in [32,64]:
        for epochs in [5,10]:
            with mlflow.start_run():
                mlflow.log_param("batch_size", batch_size)
                mlflow.log_param("epochs", epochs)
                # train model
                model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(x_test, y_test))
                # log model
                mlflow.keras.log_model(model, f"fashion_mnist_model_{batch_size}_{epochs}")
                # evaluate and log metrics
                test_loss, test_acc = model.evaluate(x_test, y_test)
                mlflow.log_metric("test_accuracy", test_acc)
                print(f"Test accuracy:{test_acc}")

    # Retrieving and using the best model
    best_model = mlflow.keras.load_model('models:/fashion_mnist_model/Production')