import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, None, 30, None, 22],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'Houston']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Fill with specific values
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': 0,
    'City': 'Unknown'
})

print("\nDataFrame with missing values filled with specific values:")
print(df_filled)

# Fill numeric columns with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nDataFrame with numeric missing values filled with the mean:")
print(df)

# Forward fill
df_ffill = df.fillna(method='ffill')

print("\nDataFrame with forward fill:")
print(df_ffill)

# Backward fill
df_bfill = df.fillna(method='bfill')

print("\nDataFrame with backward fill:")
print(df_bfill)
