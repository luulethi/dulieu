import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load and preprocess data
df_sales = pd.read_csv('Cleaned_Sales.csv')
df_sales['SalesDate'] = pd.to_datetime(df_sales['SalesDate'])
df_sales['Month'] = df_sales['SalesDate'].dt.month
df_sales['Year'] = df_sales['SalesDate'].dt.year

# Features and target variable
X = df_sales[['Quantity']]
y = df_sales['Revenue']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)



# Plotting the prediction for future quantity
future_quantity = pd.DataFrame({'Quantity': [10]})
future_sales = model.predict(future_quantity)

plt.figure(figsize=(10, 6))
plt.bar(['Predicted Revenue for 10 units'], [future_sales[0]], color='teal')
plt.title('Predicted Revenue for Future Quantity')
plt.xlabel('Quantity')
plt.ylabel('Predicted Revenue')
plt.grid(True)
plt.show()





# # Calculating residuals
# residuals = y_test - y_pred
# # Plotting residuals
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=y_pred, y=residuals, color='purple')
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Residual Plot')
# plt.xlabel('Predicted Revenue')
# plt.ylabel('Residuals')
# plt.grid(True)
# plt.show()






# # Plotting the training data and the regression line
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=X_train['Quantity'], y=y_train, color='blue', label='Training Data')
# sns.scatterplot(x=X_test['Quantity'], y=y_test, color='green', label='Test Data')
# plt.plot(X_test, y_pred, color='red', label='Regression Line')
# plt.title('Scatter Plot with Regression Line')
# plt.xlabel('Quantity Sold')
# plt.ylabel('Revenue')
# plt.legend()
# plt.grid(True)
# plt.show()















# print(f"Mean Squared Error: {mse:.2f}")
# print(f"R-squared: {r2:.2f}")

# # Predict future sales (example for quantity of 10 units)
# future_quantity = pd.DataFrame({'Quantity': [10]})
# future_sales = model.predict(future_quantity)
# print(f"Predicted Revenue for 10 units: ${future_sales[0]:.2f}")
