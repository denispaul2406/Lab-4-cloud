# app.py
import warnings
import pandas as pd
from sklearn import model_selection
import numpy as np
import sklearn
from sklearn import linear_model


def main():
    X = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
    y = [8, 10, 12, 14, 16, 18, 20]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=7)
    print("Training Features", X_train)
    print("Training Labels", y_train)
    print("Testing Features", X_test)
    print("Testing Labels", y_test)
    reg = linear_model.LinearRegression()
    reg.fit(X_train, y_train)
    # Accuracy on test set
    result = reg.score(X_test, y_test)
    print("Accuracy - test set: %.2f%%" % (result * 100.0))
    X_height = [[12.0]]
    print("Prediction for X_height:", reg.predict(X_height))


if __name__ == "__main__":
    main()
