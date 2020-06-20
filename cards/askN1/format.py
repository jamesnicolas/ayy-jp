import os
import glob
import sys
from dataclasses import dataclass
from typing import Callable, List, Dict
from convert import kanji, kana
"""
format.py reads all the .ankle files, puts them into memory, then processes them sequentially.
Files need to be processed sequentially because some of the fields depend on their previous inputs.
"""

@dataclass
class field():
    index: int
    name: str
    param: str = ""
    func: Callable[[str,str], str] = lambda x,y: x

class card():
    def __init__(self):
        self.fields = {}
        self.index = 0
    order = [
        "Vocabulary-Kanji",
        "Vocabulary-Furigana",
        "Vocabulary-Kana",
        "Definition-English",
        "Definition-Japanese",
        "Vocabulary-Audio",
        "Vocabulary-Pos",
        "Caution",
        "Sentence-Kanji",
        "Sentence-Furigana",
        "Sentence-Kana",
        "Sentence-English",
        "Sentence-Clozed",
        "Sentence-Audio",
        "Sentence-Image",
        "Notes",
        "Core-Index",
        "Optimized-Voc-Index",
        "Ask-N1-Index",
        "Show-JJ",
        "Show-JE",
        "Tags",
    ]
    # add special fields
    def special_fields(self):
        rules = {
            "Vocabulary-Kanji": kanji(self.fields["Vocabulary-Furigana"]),
            "Vocabulary-Kana": kana(self.fields["Vocabulary-Furigana"]),
            "Sentence-Kana": kana(self.fields["Sentence-Furigana"]),
            "Sentence-Kanji": kanji(self.fields["Sentence-Furigana"]),
            "Vocabulary-Audio": "[sound:{:04d}.mp3]".format(self.index),
            "Optimized-Voc-Index": "{:04d}".format(6000 + self.index),
            "Ask-N1-Index": "{:d}".format(self.index),
            "Show-JJ": "true",
        }
        self.fields.update(rules)
        return self

    @classmethod
    def from_file(cls, filename):
        index = int(filename.split(".")[0])
        c = cls()
        c.index = index
        # add all present fields
        with open(filename, encoding='utf8') as f:
            for line in f:
                line = line.rstrip()
                parts = line.split("#")
                c.fields[parts[1]] = parts[0]
        c.special_fields()
        return c
    
    def get_field_by_name(self, name):
        for field in self.fields:
            if field["name"] == name:
                return field
        return None

    #scd is semi-colon delimited format
    def to_scd(self):
        scd = ""
        for i in self.fields:
            scd += self.fields[i]
            scd += ";"
        return scd

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
        output += card.from_file(file["name"]).to_scd()
        output += "\n"
    o.write(output)