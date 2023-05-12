from datetime import datetime
from DataParser import DataParser

start_time = datetime.now()
a = DataParser("temp_q60.wpilog")

print("Time to completion")
print("==================")
print(datetime.now() - start_time)
