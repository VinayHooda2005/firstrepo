import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Dataset
data = {
    "area": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "bedrooms": [2, 2, 3, 3, 4, 4, 4, 5],
    "age": [10, 8, 5, 4, 2, 3, 1, 2],
    "price": [30, 38, 50, 62, 78, 80, 90, 105]
}

df = pd.DataFrame(data)

# Features and target
X = df[["area", "bedrooms", "age"]]
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Model
model = LinearRegression()

# Training
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Predict a new house
new_house = pd.DataFrame({
    "area": [1300],
    "bedrooms": [3],
    "age": [4]
})

print("Predicted price:", model.predict(new_house)[0])