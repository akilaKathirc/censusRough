import os
from dotenv import load_dotenv
import pymongo
import pyodbc

# MongoDB Connection
load_dotenv(".env")
mongo_client = pymongo.MongoClient(os.getenv("MongoClient"))
mongo_db = mongo_client["GuviCensusData"]
mongo_collection = mongo_db["census"]

# Fetch data from MongoDB
mongo_data = list(mongo_collection.find())

# MSSQL Connection
mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-3VBDJOUV;'
    'DATABASE=Census;'
    'UID=aki;'
    'PWD=aki'
)
mssql_cursor = mssql_conn.cursor()


# Function to dynamically create an insert query
def create_insert_query(table_name, document):
    columns = ", ".join(document.keys())
    placeholders = ", ".join("?" for _ in document.values())
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    return query

# Define your insert query for MSSQL
insert_query = """
INSERT INTO your_sql_table (field1, field2, field3)
VALUES (?, ?, ?)
"""

# Transfer data from MongoDB to MSSQL
table_name = "your_sql_table"
for document in mongo_data:
    # Ensure document has valid data and convert ObjectId to string if present
    document = {k: str(v) if isinstance(v, pymongo.objectid.ObjectId) else v for k, v in document.items()}
    insert_query = create_insert_query(table_name, document)
    values = list(document.values())
    
    # Execute the insert query
    mssql_cursor.execute(insert_query, values)

# Commit the transaction
mssql_conn.commit()

# Close the connections
mssql_cursor.close()
mssql_conn.close()
mongo_client.close()
