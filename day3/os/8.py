import os
import datetime

p = "/Users/shobhit/Desktop/qti_pythoneers/day3/os/3.py"

objs = os.stat(p)

modified_time = datetime.datetime.fromtimestamp(objs.st_mtime)

print(modified_time)
