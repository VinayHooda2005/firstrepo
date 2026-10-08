import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Dataset
data = {
    "hours": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6,
              6, 7, 7, 8, 8, 9, 9, 10, 10, 11],
    "attendance": [40, 45, 50, 55, 60, 60, 65, 65, 70, 70,
                   75, 75, 80, 80, 85, 85, 90, 90, 95, 95],
    "result": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input and output
X = df[["hours", "attendance"]]
y = df["result"]

# Train-test split with class balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create model
model = LogisticRegression()

# Training
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Probability predictions
y_prob = model.predict_proba(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=0))

# New student
new_student = pd.DataFrame({
    "hours": [7],
    "attendance": [80]
})

prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("Predicted class:", prediction[0])
print("Fail probability:", probability[0][0])
print("Pass probability:", probability[0][1])