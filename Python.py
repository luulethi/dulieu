import pandas as pd
# Read data from CSV files
df_country = pd.read_csv('Country.csv')
df_customer = pd.read_csv('Customer.csv')
df_market = pd.read_csv('Market.csv')
df_product = pd.read_csv('Product.csv')
df_sales = pd.read_csv('Sales.csv')

# Display the first 5 rows of each dataframe
print("Country Data:\n", df_country.head())
print("\nCustomer Data:\n", df_customer.head())
print("\nMarket Data:\n", df_market.head())
print("\nProduct Data:\n", df_product.head())
print("\nSales Data:\n", df_sales.head())

# Handling missing values
df_country.fillna({'Population': df_country['Population'].mean(), 'GDP': df_country['GDP'].mean()}, inplace=True)
df_customer.dropna(subset=['CustomerName', 'ContactNumber'], inplace=True)
df_market.dropna(subset=['MarketName', 'MarketType'], inplace=True)
df_product.dropna(subset=['ProductName', 'Category', 'UnitPrice', 'CostPrice'], inplace=True)
df_sales.dropna(subset=['SalesDate', 'Quantity', 'Revenue', 'KPIProfit'], inplace=True)

# Convert data types if necessary
df_sales['SalesDate'] = pd.to_datetime(df_sales['SalesDate'])

# Handling erroneous values
df_sales = df_sales[df_sales['Quantity'] > 0]
df_sales = df_sales[df_sales['Revenue'] >= 0]

# Save cleaned data to new CSV files
df_country.to_csv('Cleaned_Country.csv', index=False)
df_customer.to_csv('Cleaned_Customer.csv', index=False)
df_market.to_csv('Cleaned_Market.csv', index=False)
df_product.to_csv('Cleaned_Product.csv', index=False)
df_sales.to_csv('Cleaned_Sales.csv', index=False)

# Display cleaned data
print("\nCleaned Sales Data:\n", df_sales.head())
