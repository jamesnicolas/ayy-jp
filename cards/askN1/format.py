import os
import sys

index = sys.argv[1]

with open('%s.txt' % (index), encoding='utf8') as f:
    with open('anki-%s.txt' % (index), 'w+', encoding='utf8') as o:
        output = "# This file is auto generated.\n"
        for i, line in enumerate(f):
            words = line.split("#")
            output += words[0] + ";"
        o.write(output)
        