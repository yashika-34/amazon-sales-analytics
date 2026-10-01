import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/amazon_cleaned.csv")

# Revenue by Category
category_sales = df.groupby("Category")["TotalAmount"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
category_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.tight_layout()
plt.savefig("visuals/category_revenue.png")
plt.close()

# Revenue by Payment Method
payment_sales = df.groupby("PaymentMethod")["TotalAmount"].sum()

plt.figure(figsize=(8,5))
payment_sales.plot(kind="bar")
plt.title("Revenue by Payment Method")
plt.tight_layout()
plt.savefig("visuals/payment_revenue.png")
plt.close()

# Order Status Distribution
status_counts = df["OrderStatus"].value_counts()

plt.figure(figsize=(6,6))
status_counts.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Order Status Distribution")
plt.savefig("visuals/order_status.png")
plt.close()

print("EDA Completed")