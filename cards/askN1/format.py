import os
import glob
import sys

# get all .ankle files and sort them
ankles = []
for file in glob.glob("*.ankle"):
    num = int(file.split(".")[0])
    ankles.append({"index":num, "name":file})
ankles.sort(key=lambda x: x["index"])

# loop through all the .ankle files in order and compile it into deck.txt
with open('deck.txt', 'w+', encoding='utf8') as o:
    output = "# J-J cards. This file is auto generated.\n"
    for file in ankles:
        with open('{}.ankle'.format(file["index"]), encoding='utf8') as f:
            for i, line in enumerate(f):
                parts = line.split("#")
                output += parts[0] + ";"
            output += "\n"
    o.write(output)