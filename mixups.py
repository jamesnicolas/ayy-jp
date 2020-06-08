with open('mixups.txt', encoding='utf8') as f:
    for line in f:
        words = line.split()
        words.sort()
        output = '　'.join(words)
        print(output)
