import pandas as pd

df = pd.read_csv("data/raw/Amazon.csv")

print(df.shape)
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df.to_csv("data/cleaned/amazon_cleaned.csv", index=False)

print("Cleaned Dataset Saved")