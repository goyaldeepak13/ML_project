import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):# whenever an exception gets raised i wan to push this on my own custom message and this error detial will basically be present inside the sys
    
    _,_,exc_tb = error_detail.exc_info()   # this varible exc_tb will probably give you all the information like on which file exception occured on which line no the exception occured
    
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
     



class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
 


        

    

    # if __name__ == "__main__":
    #     try:
    #         a = 1/0
    #     except Exception as e:
    #         logging.info("Divide by Zero")
    #         raise CustomException(e,sys)  
