import os


from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv


load_dotenv(".env")
client=MongoClient(os.getenv("MongoClient"))

db=client.GuviCensusData
collection=db.CensusData_2011

def insert_censusdata_2011(df):
    # Convert DataFrame to dictionary format and insert into MongoDB
    collection.insert_many(df.to_dict('records'))
    # a={"key":period, "income":income,"expenses": expenses , "comment":comment}
    # collection.insert_one(a)


def fetch_all_periods():
    return collection.find()

# a= fetch_all_periods()
# print(a)
# for i in a:
#     print(i)
# def get_period(period):
    # a = collection.find({"key":period})
    # for i in a:
    #     return i