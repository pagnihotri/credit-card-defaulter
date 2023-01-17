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
from defaulter.components.data_validation import DataValidation
from defaulter.components.data_transformation import DataTransformation
from defaulter.components.model_trainer import ModelTrainer

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
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact= data_ingestion.initiate_data_ingestion()
          

          data_validation_config=config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_validation_artifact = data_validation.initiate_data_validation()

          data_transformation_config=config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
          data_transformation = DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_transformation_artifact = data_transformation.initiate_data_transformation()

          model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
          model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact = model_trainer.initiate_model_trainer()
     except Exception as e:
          print(e) 
