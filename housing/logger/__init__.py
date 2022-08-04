import logging
from datetime import datetime
import pandas as pd
import os
LOG_DIR="logs"

def get_file_name():
    return f"log_{get_current_time_stamp()}.log"


LOG_FILE_NAME =get_file_name()

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH =os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcname)s()^;%(message)s',
level=logging.INFO
)

def get_log_data_frame(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines()
        data.append(line.split("^;"))
    
    log_df=pd.DataFrame(data)
    columns=["Time Stamp", "Log level", "Line Number","Function Name", "Message"]
    log_df.columns=columns

    log_df["Log_Message"]=log_df["Time Stamp"].astype(str) + ":$" +log_df["message"]

    return log_df[["log_message"]]