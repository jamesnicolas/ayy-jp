import os
import glob
import sys

"""
format.py reads all the .ankle files, puts them into memory, then processes them sequentially.
Files need to be processed sequentially because some of the fields depend on their previous inputs.
"""

ankle = {
    "Vocabulary-Kanji": {
        "index":0,
        "func":"$kanji(Vocabulary-Furigana)"
    },
    "Vocabulary-Furigana":{"index":1},
    "Vocabulary-Kana": {
        "index":2,
        "func":"$kana(Vocabulary-Furigana)"
    },
    "Definition-English":{"index":3},
    "Definition-Japanese":{"index":4},
    "Vocabulary-Audio":{"index":5},
    "Vocabulary-Pos":{"index":6},
    "Caution":{"index":7},
    "Sentence-Kanji":{"index":8},
    "Sentence-Furigana":{"index":9},
    "Sentence-Kana":{"index":10},
    "Sentence-English":{"index":11},
    "Sentence-Clozed":{"index":12},
    "Sentence-Audio":{"index":13},
    "Sentence-Image":{"index":14},
    "Notes":{"index":15},
    "Core-Index":{"index":16},
    "Optimized-Voc-Index":{"index":17},
    "Ask-N1-Index":{"index":18},
    "Show-JJ":{"index":19},
    "Show-JE":{"index":20},
    "Tags":{"index":21},
}

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