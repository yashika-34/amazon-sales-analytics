import pandas as pd

df = pd.read_csv("data/cleaned/amazon_cleaned.csv")

print("\nTOP 10 PRODUCTS BY REVENUE")
print(
    df.groupby("ProductName")["TotalAmount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTOP 10 CATEGORIES BY REVENUE")
print(
    df.groupby("Category")["TotalAmount"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTOP 10 CITIES BY REVENUE")
print(
    df.groupby("City")["TotalAmount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTOP 10 BRANDS BY REVENUE")
print(
    df.groupby("Brand")["TotalAmount"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nPAYMENT METHOD DISTRIBUTION")
print(df["PaymentMethod"].value_counts())