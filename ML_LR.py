import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv('Cleaned_Sales.csv')
df = pd.read_csv('Cleaned_Sales.csv')

# Define features and target
X = df[['Quantity']]
y = df['Revenue']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

df = pd.read_csv('Cleaned_Sales.csv')



# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [1000, 1500, 1200, 1700, 1600]

# Plotting line chart
plt.figure(figsize=(10, 6))
sns.lineplot(x=months, y=sales, marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()




