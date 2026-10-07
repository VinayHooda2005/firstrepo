import numpy as np
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
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "marks": [15, 20, 35, 40, 50, 60, 65, 75, 85, 95]
}

df = pd.DataFrame(data)

# Features and target
X = df[["hours"]]
y = df["marks"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

# New prediction
new_student = pd.DataFrame({"hours": [7.5]})
prediction = model.predict(new_student)

print("Predicted marks:", prediction[0])