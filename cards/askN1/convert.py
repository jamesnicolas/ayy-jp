import re
import sys, os, re, subprocess
import pykakasi
from dataclasses import dataclass
# patterns adapted from anki source code
# https://github.com/ankitects/anki/blob/ee27711b65a97ba3db2ec19dcaf99791600d9985/rslib/src/template_filters.rs#L101

def kanji(furigana):
    remove_space = re.sub(' ', '',furigana)
    pattern = r'\[[^\]]*\]'
    remove_brackets = re.sub(pattern, '', remove_space)
    return remove_brackets

def kana(furigana):
    pattern = r' ?([^ >]+?)\['
    remove_kanji = re.sub(pattern, '', furigana)
    remove_closing = re.sub(']', '', remove_kanji)
    return remove_closing

@dataclass
class testCase():
    name: str
    furigana : str
    expected_kana : str
    expected_kanji : str

tests = [
    testCase(
        "normal case",
        "身内[みうち]に 医者[いしゃ]がいると、 何[なに]かと 安心[あんしん]だ",
        "みうちにいしゃがいると、なにかとあんしんだ",
        "身内に医者がいると、何かと安心だ",
    ),
    testCase(
        "no ruby",
        "empty",
        "empty",
        "empty",
    ),
    testCase(
        "anki's test",
        "test first[second] third[fourth]",
        "testsecondfourth",
        "testfirstthird",
    ),
]

def test():
    for t in tests:
        if (kanji(t.furigana) != t.expected_kanji):
            print("Kanji: case {} failed".format(t.name))
            print("Kanji: Expected {}".format(t.expected_kanji))
            print("Kanji: Got {}".format(kanji(t.furigana)))

        if (kana(t.furigana) != t.expected_kana):
            print("Kana: case {} failed".format(t.name))
            print("Kana: Expected {}".format(t.expected_kana))
            print("Kana: Got {}".format(kana(t.furigana)))
