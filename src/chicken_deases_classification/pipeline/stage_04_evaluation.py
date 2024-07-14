import sys
sys.path.append('F:\FAHIM\Data Science\y_ml_project\p2')
from src.chicken_deases_classification.config.configuration import ConfigurationManager
from src.chicken_deases_classification.componenets.prepare_base_model import PrepareBaseModel
from src.chicken_deases_classification import logger
from src.chicken_deases_classification.exception import CustomException,error_message_detail
from src.chicken_deases_classification.componenets.prepared_callbacks import PrepareCallback
from src.chicken_deases_classification.componenets.training import Training
from src.chicken_deases_classification.componenets.evaluation import Evaluation


STAGE_NAME = 'Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<')
        obj =ModelEvaluationPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} finished <<<')
    except CustomException as e:
        logger.exception(e)
        raise error_message_detail(e,sys)