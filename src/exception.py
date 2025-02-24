import sys # sys tracks all the exceptions
import logging
import logger # import the previously created logger file into this file so that the logs are tracked.

def error_message_detail(error, error_detail:sys):  # error_detail is present inside sys.
    _,_,exc_tb=error_detail.exc_info() # exc_tb gives detials of the exception or error
    file_name=exc_tb.tc_frame.f_code.co_filename # it gives the file name where the error occured
    error_message="Error occured in python scirpt name: [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
        )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message # it prints the error message when the custom exception is raised.

# testing purpose 
if __name__=="__main__":
    try: 
        a = 1/0
    except Exception as e:
        logging.info("Divide by 0 error")
        raise CustomException(e,sys)
        