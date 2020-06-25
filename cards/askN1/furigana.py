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
with open('{}.ankle'.format(max_num),'r', encoding='utf8') as curr_file:
    for i, line in enumerate(curr_file):
        parts = line.split("#")
        field_name = parts[1].rstrip()
        order.append(field_name)
        if field_name in ["Vocabulary-Furigana", "Sentence-Furigana", "Definition-Furigana"]:
            fields[field_name] = mecab.reading(parts[0])
        else:
            fields[field_name] = parts[0]

with open('{}.ankle'.format(max_num),'w', encoding='utf8') as curr_file:
    output = ""
    for i, v in enumerate(order):
        output += "{}#{}{}".format(fields[v],v,"\n" if i < len(order)-1 else "")
    curr_file.write(output)
