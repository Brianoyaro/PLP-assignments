import pandas as pd
import matplotlib.pyplot as plt

# Apply a consistent style
plt.style.use("seaborn-v0_8")

'''Task 1'''
# load csv
df = pd.read_csv("Walmart_Sales.csv")

# Show first 5 rows
print("Preview of Dataset:")
print(df.head(), "\n")

# Info about dataset
print("Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("Missing Values per Column:")
print(df.isnull().sum(), "\n")

'''Task 2'''
print("Statistical Summary of Numerical Columns:")
print(df.describe(), "\n")

# Grouping: Average Weekly Sales by Store
avg_sales_per_store = df.groupby("Store")["Weekly_Sales"].mean()
print("Average Weekly Sales per Store:")
print(avg_sales_per_store.head(), "\n")

# Identify best-performing store
best_store = avg_sales_per_store.idxmax()
best_sales = avg_sales_per_store.max()
print(f"Best Performing Store: {best_store} with Average Sales = {best_sales:.2f}\n")

# Identify worst-performing store
worst_store = avg_sales_per_store.idxmin()
worst_sales = avg_sales_per_store.min()
print(f"Worst Performing Store: {worst_store} with Average Sales = {worst_sales:.2f}\n")

'''Task 3'''
'''# Line chart: Weekly Sales over Time for Store 1
plt.figure(figsize=(8,5))
store1 = df[df["Store"] == 1]
plt.plot(store1["Date"], store1["Weekly_Sales"], marker="o", color="blue")
plt.title("Weekly Sales Trend for Store 1")
plt.xlabel("Date")
plt.ylabel("Weekly Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Filter Store 1 data
store1 = df[df["Store"] == 1]

# Line chart
plt.figure(figsize=(10,6))
plt.plot(store1["Date"], store1["Weekly_Sales"], marker="o", color="blue")

plt.title("Weekly Sales Trend for Store 1")
plt.xlabel("Date")
plt.ylabel("Weekly Sales")

# Format x-axis: show fewer ticks
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # show ~10 evenly spaced dates

plt.tight_layout()
plt.show()


# Bar chart: Average Weekly Sales per Store (Top 10 for readability)
plt.figure(figsize=(8,5))
avg_sales_per_store.sort_values(ascending=False).head(10).plot(kind="bar", color="green")
plt.title("Top 10 Stores by Average Weekly Sales")
plt.xlabel("Store")
plt.ylabel("Average Weekly Sales")
plt.show()

# Histogram: Distribution of Weekly Sales
plt.figure(figsize=(8,5))
df["Weekly_Sales"].hist(bins=30, color="orange", edgecolor="black")
plt.title("Distribution of Weekly Sales")
plt.xlabel("Weekly Sales")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Temperature vs Weekly Sales
plt.figure(figsize=(8,5))
plt.scatter(df["Temperature"], df["Weekly_Sales"], alpha=0.5, color="purple")
plt.title("Temperature vs Weekly Sales")
plt.xlabel("Temperature")
plt.ylabel("Weekly Sales")
plt.show()

'''Reporting'''
print("Findings & Observations:")
print("- Sales fluctuate heavily over time for individual stores.")
print("- Some stores consistently outperform others.")
print("- Weekly sales distribution is skewed in the sense that many weeks have lower sales while few have very high sales.")
print("- Temperature does not have a strong visible correlation with weekly sales.")
