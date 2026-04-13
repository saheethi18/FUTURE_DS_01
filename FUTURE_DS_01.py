# ================================
# BUSINESS SALES PERFORMANCE ANALYTICS
# ================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv('sales_data.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Extract Month
df['Month'] = df['Date'].dt.to_period('M')

# -------------------------------
# BASIC INFO
# -------------------------------
print("Dataset Preview:\n", df.head())
print("\nTotal Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

# -------------------------------
# 1. MONTHLY SALES TREND
# -------------------------------
monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMonthly Sales:\n", monthly_sales)

plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 2. TOP SELLING PRODUCTS
# -------------------------------
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

print("\nTop Selling Products:\n", product_sales)

plt.figure()
product_sales.plot(kind='bar')
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 3. REGION-WISE PERFORMANCE
# -------------------------------
region_sales = df.groupby('Region')['Sales'].sum()

print("\nSales by Region:\n", region_sales)

plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 4. PROFIT ANALYSIS
# -------------------------------
profit_product = df.groupby('Product')['Profit'].sum()

print("\nProfit by Product:\n", profit_product)

plt.figure()
profit_product.plot(kind='bar')
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.show()

# -------------------------------
# 5. TOP REGION
# -------------------------------
top_region = region_sales.idxmax()
print("\nTop Performing Region:", top_region)

# -------------------------------
# 6. BEST PRODUCT
# -------------------------------
top_product = product_sales.idxmax()
print("Top Selling Product:", top_product)

# -------------------------------
# END
# -------------------------------
