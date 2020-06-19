import re

def kanji(furigana):
    remove_space = re.sub(' ', '',furigana)
    pattern = r'\[[^\]]*\]'
    remove_brackets = re.sub(pattern, '', remove_space)
    return remove_brackets

def kana(furigana):
    pattern = r' [^\[]*\['
    remove_kanji = re.sub(pattern, '', furigana)
    remove_closing = re.sub(']', '', remove_kanji)
    return remove_closing

furigana = "身内[みうち]に 医者[いしゃ]がいると、 何[なに]かと 安心[あんしん]だ"
expected_kana = "みうちにいしゃがいると、なにかとあんしんだ"
expected_kanji = "身内に医者がいると、何かと安心だ"

if (kanji(furigana) != expected_kanji):
    print("Expected {}".format(expected_kanji))
    print("Got {}".format(kanji(furigana)))

if (kana(furigana) != expected_kana):
    print("Expected {}".format(expected_kana))
    print("Got {}".format(kana(furigana)))