from src.chicken_deases_classification import logger
from src.chicken_deases_classification.pipeline.stage_01_data_ingestion import DataIngestionTraininPipeline
from src.chicken_deases_classification.exception import CustomException
from src.chicken_deases_classification.exception import error_message_detail
import sys

STAGE_NAME =' Data Ingestion Stage'

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<')
    obj = DataIngestionTraininPipeline()
    obj.main()
    logger.info(f'>>>>> stage {STAGE_NAME} finished <<<')
except CustomException as e:
    logger.exception(e)
    raise error_message_detail(e, sys)