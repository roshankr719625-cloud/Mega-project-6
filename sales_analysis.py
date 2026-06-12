import pandas as pd
import matplotlib.pyplot as plt



data = {
    "Product": ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse"],
    "Month": ["Jan", "jan", "feb", "feb", "mar"],
    "Quantity": [2, 10, 1, 5, 20],
    "Price": [50000, 500, 50000, 1000, 500]

}
df = pd.DataFrame(data)

df["Revenue"] = df["Quantity"] * df["Price"]
# print(df)

best_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
# print(best_product)

total_revenue = df["Revenue"].sum()
# print("Total Revenue:", total_revenue)

monthly_sales = df.groupby("Month")["Revenue"].sum()
# print(monthly_sales)

monthly_sales.plot(kind="bar")
plt.title("Monthly sales analysis")
plt.ylabel("Revenue")
plt.show()
