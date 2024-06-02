# def TelanganaData():
#     with open(r'Data/Telengana.txt') as f:
#         testsite_array=f.readlines()
#         print(testsite_array)



# TelanganaData()


# from pathlib import Path

# p = Path(__file__).with_name('Telangana.txt')
# with p.open('r') as f:
#     print(f.read())


from pathlib import Path
from pyspark.sql.functions import col, when
import pandas as pd


def open_file_with_pathlib(file_name):
   script_dir = Path(__file__).resolve().parent
   file_path = script_dir / file_name

   with open(file_path, 'r') as file:
      lines = [line.strip() for line in file.readlines()]
      return list(lines)

def updateDFValue():
    file_path = 'census_2011.csv'  # replace with the correct file path
    data = pd.read_csv(file_path)
    ct = open_file_with_pathlib("Data\Telangana.txt")
    for distictName in ct:
        data.loc[data['District name'] == distictName, 'State name'] = 'Telangana'
    print(data[data['State name'] == 'Telangana'])


updateDFValue()
# filtered_df = df[df['State name'] == 'Telangana']
# print(filtered_df)



