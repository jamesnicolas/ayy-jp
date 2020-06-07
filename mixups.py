import fileinput

for line in fileinput.input("mixups.txt", inplace=True):
    words = line.split()
    words.sort()
    output = '　'.join(words)
    print(output)
