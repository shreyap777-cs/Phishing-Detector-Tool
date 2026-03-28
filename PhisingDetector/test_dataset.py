import pandas as pd

df = pd.read_csv("dataset.csv", encoding='latin-1')

# Keep only required columns
df = df[['v1', 'v2']]

# Rename columns (important for next steps)
df.columns = ['label', 'text']

print(df.head())
print(df.columns)