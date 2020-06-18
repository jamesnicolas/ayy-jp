import os
import sys
import glob

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
for file in glob.glob("*.ankle"):
    num = int(file.split(".")[0])
    if num > max_num:
        max_num = num

# store fields of previous card so we can possibly perform operations on it
prev_fields = {}
with open('{}.ankle'.format(max_num), encoding='utf8') as prev_file:
    for i, line in enumerate(prev_file):
        parts = line.split("#")
        prev_fields[parts[1]] = parts[0]

output = ""
# generate the new file based on the previous card and the format file
with open('format.txt', encoding='utf8') as format_file:
    for i, line in enumerate(format_file):
        """
        a line in format.txt looks like
        $inc#Vocabulary-Index
        so we're going to look at the previous file's "Vocabulary-Index"
        and apply the $inc function defined in ops, and save that as the new value
        """
        parts = line.split("#")
        field_name = parts[1]
        value = parts[0]
        prev_value = prev_fields[field_name]
        value = op(value,prev_value)
        output += "#".join([value,field_name])

with open('{}.ankle'.format(max_num+1), 'w+', encoding='utf8') as new_file:
    if (output != ""):
        new_file.write(output)