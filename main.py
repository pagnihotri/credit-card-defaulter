#from sensor.pipeline.training_pipeline import start_training_pipeline
#from sensor.pipeline.batch_prediction import start_batch_prediction
from defaulter.logger import logging
from defaulter.exception import DefaulterException
#from defaulter.utils import get_collection_as_dataframe
import sys,os
from defaulter.entity import config_entity
from defaulter.entity.config_entity import DataIngestionConfig
from defaulter.components import data_ingestion
from defaulter.components.data_ingestion import DataIngestion

#file_path="/config/workspace/aps_failure_training_set1.csv"
#print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          #output_file = start_batch_prediction(input_file_path=file_path)
          #print(output_file)
          #get_collection_as_dataframe(database_name='creditcard', collection_name='defaulter')
          training_pipeline_config=config_entity.TrainingPipelineConfig()
          data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
          print(e) 
