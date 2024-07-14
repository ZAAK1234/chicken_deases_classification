import sys
sys.path.append('F:\FAHIM\Data Science\y_ml_project\p2')
from src.chicken_deases_classification.config.configuration import ConfigurationManager
from src.chicken_deases_classification.componenets.prepare_base_model import PrepareBaseModel
from src.chicken_deases_classification import logger
from src.chicken_deases_classification.exception import CustomException,error_message_detail



STAGE_NAME = 'Data Ingestion stage'


class PrepareBaseModelTraininPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<')
        obj = PrepareBaseModelTraininPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} finished <<<')
    except CustomException as e:
        logger.exception(e)
        raise error_message_detail(e,sys)