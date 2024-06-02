import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'census_2011.csv'
df = pd.read_csv(file_path)

# Calculate the initial percentage of missing data for each column
initial_missing_data = df.isnull().mean() * 100
print(initial_missing_data)
fni_missing_data = df['Power_Parity_Rs_150000_240000'].isna().sum()
print(fni_missing_data)
fn1i_missing_data = df['Power_Parity_Rs_150000_330000'].isna().sum()
print(fn1i_missing_data)
fn1iw_missing_data = df['Workers'].isna().sum()
print(fn1iw_missing_data)
lt_missing_data = df['Literate_Education'].isna().sum()
print(lt_missing_data)

if 'Power_Parity_Rs_150000_330000' in df.columns and 'Power_Parity_Rs_150000_240000' in df.columns:
       if df['Power_Parity_Rs_150000_240000'].isna().sum():
            df['Power_Parity_Rs_150000_240000'].fillna(df['Power_Parity_Rs_150000_330000'], inplace= True)
        

if 'Power_Parity_Rs_150000_330000' in df.columns and 'Power_Parity_Rs_150000_240000' in df.columns:
   if df['Power_Parity_Rs_150000_330000'].isna().sum():
       df['Power_Parity_Rs_150000_330000'].fillna(df['Power_Parity_Rs_150000_240000'], inplace= True)


worker_column = ['Male_Workers','Female_Workers']
if 'Workers' in df.columns and all(i in df.columns for i in worker_column):
    df['Workers'].fillna(df['Male_Workers'] + df['Female_Workers'], inplace=True)

edu_column=['Middle_Education','Secondary_Education','Higher_Education','Graduate_Education','Other_Education']
if 'Literate_Education' in df.columns and all(col in df.columns for col in edu_column):
     df['Literate_Education'].fillna(df[edu_column].sum(axis=1), inplace= True)



fn_missing_data = df['Power_Parity_Rs_150000_240000'].isna().sum()
print(fn_missing_data)
fn1_missing_data = df['Power_Parity_Rs_150000_330000'].isna().sum()
print(fn1_missing_data)
fw_missing_data = df['Workers'].isna().sum()
print(fw_missing_data)
ltaf_missing_data = df['Literate_Education'].isna().sum()
print(ltaf_missing_data)

