import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data from CSV files
df_country = pd.read_csv('Cleaned_Country.csv')
df_customer = pd.read_csv('Cleaned_Customer.csv')
df_market = pd.read_csv('Cleaned_Market.csv')
df_product = pd.read_csv('Cleaned_Product.csv')
df_sales = pd.read_csv('Cleaned_Sales.csv')

# # 1. Bar Chart: GDP by Country
# top_20_countries = df_country.head(20)
# plt.figure(figsize=(12, 8))
# plt.bar(top_20_countries['CountryName'], top_20_countries['GDP'], color='skyblue')
# plt.xlabel('Country')
# plt.ylabel('GDP (in billion USD)')
# plt.title('Top 20 Countries by GDP')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# # 2. Line Chart: Revenue Over Time
# plt.figure(figsize=(12, 6))
# df_sales['SalesDate'] = pd.to_datetime(df_sales['SalesDate'])
# df_sales_grouped = df_sales.groupby('SalesDate').agg({'Revenue': 'sum'}).reset_index()
# plt.plot(df_sales_grouped['SalesDate'], df_sales_grouped['Revenue'], marker='o', color='green')
# plt.xlabel('Date')
# plt.ylabel('Revenue (in USD)')
# plt.title('Revenue Over Time')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # 3. Pie Chart: Market Type Distribution
# market_counts = df_market['MarketType'].value_counts()
# plt.figure(figsize=(8, 8))
# plt.pie(market_counts, labels=market_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'gold', 'lightskyblue'])
# plt.title('Market Type Distribution')
# plt.show()

# # 4. Histogram: Distribution of Unit Prices
# plt.figure(figsize=(10, 6))
# plt.hist(df_product['UnitPrice'], bins=10, color='orange', edgecolor='black')
# plt.xlabel('Unit Price (in USD)')
# plt.ylabel('Frequency')
# plt.title('Distribution of Unit Prices')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# 5. Scatter Plot: Revenue vs. Quantity Sold
plt.figure(figsize=(12, 6))
plt.scatter(df_sales['Quantity'], df_sales['Revenue'], color='purple', alpha=0.6)
plt.xlabel('Quantity Sold')
plt.ylabel('Revenue (in USD)')
plt.title('Revenue vs. Quantity Sold')
plt.grid(True)
plt.tight_layout()
plt.show()
