import os
import sys
import glob
import subprocess
import time
from datetime import datetime

shift_from = int(input("Shift from (inclusive):"))
shift_to = int(input("Shift to (inclusive):"))
shift_by = int(input("Shift by:"))

# get latest .ankle file number
ankles = []
for f in glob.glob("*.ankle"):
    num = int(f.split(".")[0])
    if num >= shift_from and num <= shift_to:
        ankles.append(num)

if shift_by > 0:
    ankles.sort(reverse=True)
elif shift_by < 0:
    ankles.sort()
else:
    print("Shift by is 0")
    exit(1)
for i in ankles:
    #os.rename("{}.ankle".format(i),"{}.ankle".format(i+shift_by))
    print("{}.ankle".format(i),"{}.ankle".format(i+shift_by))