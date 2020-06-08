import os
import shutil

shutil.copyfile('mixups.txt', '.backup.mixups.txt')

with open('mixups.txt', encoding='utf8') as f:
    with open('tmp.txt', 'w+', encoding='utf8') as o:
        for i, line in enumerate(f):
            words = line.split()
            words.sort()
            output = ('\n' if i else '') + '　'.join(words)
            o.write(output)

os.remove('mixups.txt')
os.rename('tmp.txt', 'mixups.txt')
