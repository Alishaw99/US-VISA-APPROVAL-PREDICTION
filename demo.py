from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys



try:
    a = 1 / "10"
    
except Exception as e:    
    raise USvisaException(e, sys) from e
    
    
    



# from us_visa.constants import DATABASE_NAME

# print(DATABASE_NAME)

# # pipline  = TrainPipeline()
# # pipline.run_pipeline()
