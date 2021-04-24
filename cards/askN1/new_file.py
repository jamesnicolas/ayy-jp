import os
import sys
import glob
import subprocess
import time
from datetime import datetime

ops = {
    "$inc":lambda x: str(int(x)+1),
    "$copy":lambda x: x,
    "$inc_sound":lambda x: "[sound:{:04d}.mp3]".format(int(x[7:11])+1),
}
def op(f, x):
    func = ops.get(f)
    if func is None:
        return f
    else:
        return func(x)

# get latest .ankle file number
ankles = []
max_num = 0
lastest_file = ""
for f in glob.glob("*.ankle"):
    num = int(f.split(".")[0])
    if num > max_num:
        max_num = num
        latest_file = f

last_file_creation_time = datetime.fromtimestamp(os.path.getctime(latest_file))
time_since_last_card = datetime.now() - last_file_creation_time
print("Card took {:d}.{:03d}s to make".format(time_since_last_card.seconds, time_since_last_card.microseconds//1000))

# store fields of previous card so we can possibly perform operations on it
prev_fields = {}
with open('{}.ankle'.format(max_num), encoding='utf8') as prev_file:
    for i, line in enumerate(prev_file):
        parts = line.rstrip().split("#")
        prev_fields[parts[1]] = parts[0]

# validate that, if the previous card is not blank, that it has all the correct fields
def missing(a, m):
    o = []
    for i in a:
        if m[i] == "":
            o.append(i)
    return o

required_fields = [
    "Sentence-Furigana",
    "Vocabulary-Pos" ,
    "Definition-English",
    "Sentence-English"
]
m = missing(required_fields, prev_fields)
if prev_fields["Vocabulary-Furigana"] != "" and m:
    print("Missing fields {}".format(m))
    exit(1)


output = ""
# generate the new file based on the previous card and the format file
with open('template.anklet', encoding='utf8') as format_file:
    for i, line in enumerate(format_file):
        """
        a line in format.txt looks like
        $inc#Vocabulary-Index
        so we're going to look at the previous file's "Vocabulary-Index"
        and apply the $inc function defined in ops, and save that as the new value
        """
        parts = line.rstrip().split("#")
        field_name = parts[1]
        value = parts[0]
        prev_value = prev_fields[field_name]
        value = op(value,prev_value)
        output += "#".join([value,field_name]) +"\n"
#remove trailing newline
output = output[:-1]

new_file_name = '{}.ankle'.format(max_num+1)
with open(new_file_name, 'w+', encoding='utf8') as new_file:
    if (output != ""):
        new_file.write(output)

process = subprocess.Popen(["code", os.path.realpath(new_file_name)], shell=True)