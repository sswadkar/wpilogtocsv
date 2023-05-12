from datetime import datetime
from DataParser import DataParser

start_time = datetime.now()
data_parser = DataParser()
data_parser.convert_wpilog_to_csv("temp_q60.wpilog")

print("Time to completion")
print("==================")
print(datetime.now() - start_time)
