#time.time(): Returns the current time in seconds 
# since the Epoch (January 1, 1970, 00:00:00 UTC).

import time
current_time = time.time()
print(current_time)
print(time.ctime())#current time

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(formatted_time)
