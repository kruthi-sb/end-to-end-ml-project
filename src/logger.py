import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" # format string, the file name will be in this naming covention.
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE) # path of the log files will be current_working_directory/logs/LOG_FILE, where logs is the directory
os.makedirs(logs_path, exist_ok=True) # it creates the logs directory if it is not present.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) 

# to overwrite the functionality of the logging, 
logging.basicConfig(
    filename=LOG_FILE_PATH, # path of the log file
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # standard format of the log message 
    level = logging.INFO, # in the case of INFO only the info messages will be logged or printed.
)

"""# testing purpose
if __name__=="__main__":
    logging.info("Logging has started") # testing purpose. This should be the first log file."""
