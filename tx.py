import pandas as pd

from task5 import insert_censusdata_2011

# Load the CSV file into a DataFrame
file_path = 'census_2011.csv'
df = pd.read_csv(file_path, na_filter=True)

# Calculate the initial percentage of missing data for each column
initial_missing_data = df.isnull().mean() * 100

def fill_nan_with_sum(row, target_field, sum_fields):
    if pd.isna(row[target_field]):
        return sum(row[field] if pd.notna(row[field]) else 0 for field in sum_fields)
    else:
        return row[target_field]
    
def fill_nan_with_another_field(row, target_field, value_fields):
    if pd.isna(row[target_field]):
        return row[value_fields]
       
# Function to clean data for BSON encoding
def clean_data_for_bson(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)  # Convert object types to string
        elif pd.api.types.is_float_dtype(df[col]) or pd.api.types.is_integer_dtype(df[col]):
            df[col] = df[col].astype(float)  # Ensure numeric types are float
    return df

def fill_nan_with_diff(row, parent_field, child_field, target_field):
    if pd.isna(row[target_field]):
        row[parent_field] - row[child_field]
        value = (row[parent_field] if pd.notna(row[parent_field]) else 0) - (row[child_field] if pd.notna(row[child_field]) else 0)
        if value <0:
            return row[target_field]
        else:
            return value
    else:
        return row[target_field]
# Clean the data

# Verify the data types after cleaning
# print(cleaned_data.dtypes)



    



