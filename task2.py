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

# Function to convert state/UT names to the desired format
def format_state_name(name):
    words = name.split()
    formatted_words = [word.capitalize() if word.lower() != "and" else "and" for word in words]
    return ' '.join(formatted_words)

# Apply the function to the 'State/UT' column
data['State/UT'] = data['State/UT'].apply(format_state_name)

# Optionally, save the updated dataframe to a new Excel file
data.to_csv('renamed_census_2011.csv', index=False)

# Display the unique values in the 'State/UT' column to verify the changes
print(data['State/UT'].unique())
