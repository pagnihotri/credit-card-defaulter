import pymongo
import pandas as pd
import json
from defaulter.config import mongo_client
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://pagnihotri:root@cluster0.asd2aoy.mongodb.net/?retryWrites=true&w=majority")
#DATAFILE_PATH="https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"
#DATABASE_NAME='aps'
#COLLECTION_NAME='sensor'

#DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
#client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH='/config/workspace/UCI_Credit_Card.csv'
DATABASE_NAME="creditcard"
COLLECTION_NAME="defaulter"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f'The number of wors and columns {df.shape}')
    df.reset_index(drop=True,inplace=True)
    df.drop(columns=['ID'],inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
