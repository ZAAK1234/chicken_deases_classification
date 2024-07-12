import sys
from src.chicken_deases_classification import logger
import logging
from datetime import datetime


def error_message_detail(error,error_detail: sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message='Error Occured in python script name[{0}] line number [{1}] error message [{2}] at [{3}]'.format(
        filename,exc_tb.tb_lineno,str(error),datetime.now()
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message