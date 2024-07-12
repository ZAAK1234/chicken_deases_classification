from src.chicken_deases_classification.config.configuration import ConfigurationManager
from src.chicken_deases_classification.componenets.data_ingestion import DataIngestion
from src.chicken_deases_classification import logger
from src.chicken_deases_classification.exception import CustomException
from src.chicken_deases_classification.exception import error_message_detail
import sys
STAGE_NAME = 'Data Ingestion stage'


class DataIngestionTraininPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<')
        obj = DataIngestionTraininPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} finished <<<')
    except CustomException as e:
        logger.exception(e)
        raise error_message_detail(e,sys)