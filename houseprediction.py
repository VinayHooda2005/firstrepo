from sklearn.linear_model import LinearRegression

# Input data(area)
x = [[800], [1000], [1200], [1500], [2000]]

# Target data (price in lakh)
y = [20, 25, 30, 38, 50]

# Create model
model = LinearRegression()

# Train model
model.fit(x,y)

# Predict price for 1300 sq ft
prediction = model.predict([[1300]])

print(prediction)