import pymongo
import pandas as pd
import json
#provide Mongodb local host url to connect to python
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Number of rows and Columns: {df.shape}")

    #convert dataframe into json so that we can store these in MongoDB
    df.reset_index(inplace=True, drop=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json records into MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)