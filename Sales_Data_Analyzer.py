import pandas as pd
import os
import matplotlib.pyplot as plt

if not os.path.exists("sales.csv"):
    print("Error: CSV file not found!")
    raise SystemExit
try:
    df = pd.read_csv("sales.csv")
except Exception:
    print("Could not read the file")
    raise SystemExit    
if df.empty:
    print("The CSV file is empty!")
    raise SystemExit

print("-----------------------")

num_rows , num_cols = df.shape

print(f"Rows: {num_rows}, Columns: {num_cols}")
print(df.head(5))
df.info()
print(df.isnull().sum())

print("-----------------------")

valid_columns = df[["quantity", "unit_price", "cost"]].select_dtypes(include="number")
invalid_columns = df[["quantity", "unit_price", "cost"]].select_dtypes(exclude="number")
if invalid_columns.empty :
    print("All columns are numeric")
else:
    print(f"Invalid columns: {invalid_columns.columns.tolist()}")

print("-----------------------")

# Sales & Profit Calculation
df["total_sales"] = df["quantity"] * df["unit_price"]
df["total_cost"] = df["quantity"] * df["cost"]
df["profit"] = df["total_sales"] - df["total_cost"]
total_revenue = df["total_sales"].sum()
total_profit = df["profit"].sum()
print(f"Total Revenue: {total_revenue}")
print(f"Total Profit: {total_profit}")

print("-----------------------")

product_sales = df.groupby("product")["total_sales"].sum()
sorted_products = product_sales.sort_values(ascending=False)
print(sorted_products)
plt.bar(sorted_products.index, sorted_products.values)
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

print("-----------------------")

best_product = product_sales.idxmax()
print(f"Best product sales: {best_product}")

category_sales = df.groupby("category")["total_sales"].sum()
shourted_catagories = category_sales.sort_values(ascending=False)
plt.bar(shourted_catagories.index, shourted_catagories.values)
plt.title("Best Catagory Sales")
plt.xlabel("Catagory")
plt.ylabel("Total Sales")
plt.grid()
plt.show()
best_category_sales = category_sales.idxmax()
print(f"best catagory sales: {best_category_sales}")

print("-----------------------")

category_profit = df.groupby("category")["profit"].sum()
shourted_profit = category_profit.sort_values(ascending=False)
plt.bar(shourted_profit.index, shourted_profit.values)
plt.title("Best Catagory Profit")
plt.xlabel("Catagory")
plt.ylabel("Profit")
plt.grid()
plt.show()
best_catagory_profit_sales = category_profit.idxmax()
best_profit_value = category_profit.max()
print(f"Highest Catagory Profit: {best_catagory_profit_sales} , By: {best_profit_value}")

print("-----------------------")

profit_margin = category_profit  / category_sales * 100
shourted_profit_margin =  profit_margin.sort_values(ascending=False)
plt.bar(shourted_profit_margin.index,shourted_profit_margin.values)
plt.title("Profit Margin For Each Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin")
plt.grid()
plt.show()
highest_profit_margin_name = profit_margin.idxmax()
highest_profit_margin_value = profit_margin.max()
print(f"Highest Catagory Profit Margin: {highest_profit_margin_name} , By: {highest_profit_margin_value:.2f}%")

print("-----------------------")

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.month_name()

months_sales = df.groupby(["month","month_name"])["total_sales"].sum()
monthly_sales = months_sales.reset_index()
print(months_sales)

plt.plot(monthly_sales["month_name"], monthly_sales["total_sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

#py -3.14 Sales_Data_Analyzer.py
