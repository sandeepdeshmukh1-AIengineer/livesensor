from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection



#def test_exception():
#    try:
#        logging.info("will get error division by zero")
#        a=1/0
#    except Exception as e:
#        raise SensorException(e,sys)


if __name__ == "__main__":
    file_path = r"D:\SENSORLIVE\aps_failure_training_reduced.csv"
    database_name="deshmukh"
    collection_name="sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)
    
    
#    try:
#        test_exception()
#    except Exception as e:
#        print(e)