from reading import MecabController
import os
import sys
import glob
import subprocess
import time

mecab = MecabController()

# get latest .ankle file number
ankles = []
max_num = 0
for file in glob.glob("*.ankle"):
    num = int(file.split(".")[0])
    if num > max_num:
        max_num = num

fields = {}
order = []
with open('{}.ankle'.format(max_num),'w+', encoding='utf8') as curr_file:
    for i, line in enumerate(curr_file):
        parts = line.split("#").rstrip()
        order.append(parts[1])
        if parts[1] in ["Vocabulary-Furigana", "Sentence-Furigana", "Definition-Furigana"]:
            fields[parts[1]] = mecab.reading(parts[0])
        else:
            fields[parts[1]] = parts[0]
    
    output = ""
    for i in order:
        output += "{}#{}\n".format(i,fields[i])
    curr_file.write(output)
