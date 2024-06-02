import pandas as pd

from task5 import insert_censusdata_2011
from tx import clean_data_for_bson, fill_nan_with_another_field, fill_nan_with_diff, fill_nan_with_sum

# Load the CSV file into a DataFrame
file_path = 'census_2011.csv'
df = pd.read_csv(file_path)
df = clean_data_for_bson(df)

# insert_censusdata_2011(filtered_data)
# Calculate the initial percentage of missing data for each column
initial_missing_data = df.isnull().mean() * 100

#########################################################################
sum_fields = ['Male_ST', 'Female_ST']
sum_fields1 = ['ST', 'Female_ST']
sum_fields2 = ['ST', 'Male_ST']

# Apply the function to each rows
df['ST'] = df.apply(lambda row: fill_nan_with_sum(row, 'ST', sum_fields), axis=1)
df['Male_ST'] = df.apply(lambda row: fill_nan_with_sum(row, 'Male_ST',sum_fields1), axis=1)
df['Female_ST'] = df.apply(lambda row: fill_nan_with_sum(row, 'Female_ST', sum_fields2), axis=1)
#########################################################################

#########################################################################
if 'SC' in df.columns and 'Male_SC' in df.columns and 'Female_SC' in df.columns:
    # print(df['SC'].isna())
    if df['SC'].empty:
        df.fillna({'SC': df['Male_SC'] + df['Female_SC']}, inplace=True)
    if  df['Male_SC'].empty:
        df.fillna({'Male_SC': df['SC'] - df['Female_SC']}, inplace=True)
    if  df['Female_SC'].empty:
        df.fillna({'Female_SC': df['SC'] - df['Male_SC']}, inplace=True)
sum_fields = ['Male_SC', 'Female_SC']
sum_fields1 = ['SC', 'Female_SC']
sum_fields2 = ['SC', 'Male_SC']

# Apply the function to each rows
print(df.apply(lambda row: fill_nan_with_sum(row, 'Female_SC', sum_fields2), axis=1))
df['SC'] = df.apply(lambda row: fill_nan_with_sum(row, 'SC', sum_fields), axis=1)
df['Male_SC'] = df.apply(lambda row: fill_nan_with_sum(row, 'Male_SC',sum_fields1), axis=1)
df['Female_SC'] = df.apply(lambda row: fill_nan_with_sum(row, 'Female_SC', sum_fields2), axis=1)
#########################################################################


#########################################################################
sum_fields2 = ['Male', 'Female']

df['Population'] = df.apply(lambda row: fill_nan_with_sum(row, 'Population', sum_fields2), axis=1)
#########################################################################

#fill_nan_with_diff(row, parent_field, child_field, target_field)
df['Male'] = df.apply(lambda row: fill_nan_with_diff(row, 'Population',  'Female', 'Male'), axis=1)


#fill_nan_with_diff(row, parent_field, child_field, target_field)
df['Female'] = df.apply(lambda row: fill_nan_with_diff(row, 'Population',  'Male', 'Female'), axis=1)
#########################################################################

# Hint: Literate = Literate_Male + Literate_Female
literacySum = ['Male_Literate', 'Female_Literate']

df['Literate'] = df.apply(lambda row: fill_nan_with_sum(row, 'Literate', literacySum), axis=1)

df['Male_Literate'] = df.apply(lambda row: fill_nan_with_diff(row, 'Literate',  'Female_Literate', 'Male_Literate'), axis=1)

df['Female_Literate'] = df.apply(lambda row: fill_nan_with_diff(row, 'Literate',  'Male_Literate', 'Female_Literate'), axis=1)
#########################################################################



#########################################################################

# Hint: Population = Young_and_Adult + Middle_Aged + Senior_Citizen + Age_Not_Stated
age_columns = ['Young_and_Adult', 'Middle_Aged', 'Senior_Citizen', 'Age_Not_Stated']

df['Population'] = df.apply(lambda row: fill_nan_with_sum(row, 'Population', age_columns), axis=1)


#########################################################################

# Hint: Households = Households_Rural + Households_Urban
# houseHolds = ['Households_Rural', 'Households_Urban']

# df['Households'] = df.apply(lambda row: fill_nan_with_sum(row, 'Households', houseHolds), axis=1)
#########################################################################


#########################################################################

# powerParity = ['Power_Parity_Rs_150000_240000']

# df['Power_Parity_Rs_150000_330000'] = df.apply(lambda row: fill_nan_with_another_field(row, 'Power_Parity_Rs_150000_330000', powerParity), axis=1)

#########################################################################
#########################################################################
# powerParity2 = ['Power_Parity_Rs_150000_330000']

# df['Power_Parity_Rs_150000_240000'] = df.apply(lambda row: fill_nan_with_another_field(row, 'Power_Parity_Rs_150000_240000', powerParity2), axis=1)
  
#########################################################################
#########################################################################
worker_column = ['Male_Workers','Female_Workers']

df['Workers'] = df.apply(lambda row: fill_nan_with_sum(row, 'Workers', worker_column), axis=1)


#########################################################################
#########################################################################




# Calculate the final percentage of missing data for each column
final_missing_data = df.isnull().mean() * 100

# Print the final missing data percentages
# print("\nFinal Missing Data Percentage for Each Column:")
# print(final_missing_data)

# Compare the initial and final missing data percentages
missing_data_comparison = pd.DataFrame({
    'Initial Missing %': initial_missing_data,
    'Final Missing %': final_missing_data
})

# print("\nMissing Data Comparison Before and After Filling:")
# print(missing_data_comparison)
df = df.fillna(0)
insert_censusdata_2011(df)
