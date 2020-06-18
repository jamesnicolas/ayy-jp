import os
import sys

index = sys.argv[1]

with open('deck.txt' % (index), 'w+', encoding='utf8') as o:
    output = "# J-J cards. This file is auto generated.\n"
    with open('%s.ankle' % (index), encoding='utf8') as f:
        for i, line in enumerate(f):
            words = line.split("#")
            output += words[0] + ";"
        output += "\n"
    o.write(output)