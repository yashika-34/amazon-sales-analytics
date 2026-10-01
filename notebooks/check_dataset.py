import pandas as pd

df = pd.read_csv("data/raw/Amazon.csv")

print("Rows, Columns:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())