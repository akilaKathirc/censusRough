import pandas as pd

# Load the Excel file
file_path = 'census_2011.csv'  # replace with the correct file path
data = pd.read_csv(file_path)

# Renaming the specified columns
renamed_columns = {
    'State name': 'State/UT',
    'District name': 'District',
    'Male_Literate': 'Literate_Male',
    'Female_Literate': 'Literate_Female',
    'Rural_Households': 'Households_Rural',
    'Urban_Households': 'Households_Urban',
    'Age_Group_0_29': 'Young_and_Adult',
    'Age_Group_30_49': 'Middle_Aged',
    'Age_Group_50': 'Senior_Citizen',
    'Age not stated': 'Age_Not_Stated'
}

# Renaming the columns in the dataframe
data.rename(columns=renamed_columns, inplace=True)

# Optionally, save the updated dataframe to a new Excel file
data.to_csv('renamed_census_2011.csv', index=False)

# Display the updated columns to verify the changes
print(data.head())
