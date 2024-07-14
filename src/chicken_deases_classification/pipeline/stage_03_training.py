import sys
sys.path.append('F:\FAHIM\Data Science\y_ml_project\p2')
from src.chicken_deases_classification.config.configuration import ConfigurationManager
from src.chicken_deases_classification.componenets.prepare_base_model import PrepareBaseModel
from src.chicken_deases_classification import logger
from src.chicken_deases_classification.exception import CustomException,error_message_detail
from src.chicken_deases_classification.componenets.prepared_callbacks import PrepareCallback
from src.chicken_deases_classification.componenets.training import Training



STAGE_NAME = 'Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callback()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<')
        obj =ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} finished <<<')
    except CustomException as e:
        logger.exception(e)
        raise error_message_detail(e,sys)
