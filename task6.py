import csv
import os
from dotenv import load_dotenv
import pymongo
import pyodbc
from collections import defaultdict
from bson import ObjectId
import pandas as pd
from sqlalchemy import create_engine


# MongoDB Connection
def clean_data(data):
    return data.fillna(0)

load_dotenv(".env")
mongo_client = pymongo.MongoClient(os.getenv("MongoClient"))
mongo_db = mongo_client["GuviCensusData"]
mongo_collection = mongo_db["CensusData_2011"]

# Fetch data from MongoDB
mongo_data = list(mongo_collection.find())

table_name = "census2011dt"

def load_data_to_mssql(data, connection_string, table_name):
    engine = create_engine(connection_string)
    data.to_sql(name=table_name, con=engine, if_exists='replace', index=False)


def process_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

# Function to infer MSSQL data types from MongoDB data types
def infer_sql_type(value):
    if isinstance(value, int):
        return "INT"
    elif isinstance(value, float):
        return "FLOAT"
    elif isinstance(value, bool):
        return "BIT"
    elif isinstance(value, str):
        return "NVARCHAR(MAX)"
    else:
        return "NVARCHAR(MAX)"  # Default to string for any other types
# print(mongo_data)
# Determine the columns and their types from the MongoDB documents
columns = defaultdict(set)

########## FOR PROCESSING OF DATA
for document in mongo_data:
    for key, value in document.items():
        columns[key].add(infer_sql_type(value))
        if isinstance(value, float):
            document[key] = process_float(value)


# Create a string for the columns in the create table statement
create_table_columns = []

for column, types in columns.items():
    # If multiple types are detected for a single column, default to NVARCHAR(MAX)
    if len(types) > 1:
        create_table_columns.append(f"[{column}] NVARCHAR(MAX)")
    else:
        create_table_columns.append(f"[{column}] {types.pop()}")


create_table_statement = f"""
CREATE TABLE {table_name} (
    {', '.join(create_table_columns)}
)
"""

# Print the CREATE TABLE statement to debug


# MSSQL Connection

mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-3VBDJOUV;'
    'DATABASE=Census;'
    'UID=aki;'
    'PWD=aki'
)
mssql_cursor = mssql_conn.cursor()

# Create the table in MSSQL
mssql_cursor.execute(f"IF OBJECT_ID('{table_name} ', 'U') IS NOT NULL DROP TABLE {table_name} ")
print(create_table_statement)
mssql_cursor.execute(create_table_statement)

# Function to dynamically create an insert query
def create_insert_query(table_name, document):
    columns = ", ".join(f"[{k}]" for k in document.keys())
    placeholders = ", ".join("?" for _ in document.values())
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    return query
# load data to sql - first method
# mssql_connection_string = "mssql+pyodbc://aki:aki@dsn"
# load_data_to_mssql(mongo_data, mssql_connection_string, table_name)
mongo_data = list(mongo_collection.find())
# Transfer data from MongoDB to MSSQL- second method
for document in mongo_data:
    # Ensure document has valid data and convert ObjectId to string if present
    document = {k: str(v) if isinstance(v, ObjectId) else v for k, v in document.items()}
    # document = process_record(document)
    # document = {k: str(v) if isinstance(v, pymongo.objectid.ObjectId) else v for k, v in document.items()}
    insert_query = create_insert_query(table_name, document)
    values = list(document.values())  
    # Execute the insert query
    mssql_cursor.execute(insert_query, values)


csv_file_path = 'mydata.csv'
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write headers
    csv_writer.writerow(mongo_data[0].keys())
    # Write data rows
    for row in mongo_data:
        csv_writer.writerow(row.values())


# Commit the transaction
mssql_conn.commit()

# Close the connections
mssql_cursor.close()
mssql_conn.close()
mongo_client.close()
