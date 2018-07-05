from ps4a import *

def test_short_words():
    assert(getWordScore("a", 7) == 1)
    assert(getWordScore("xi", 7) == 9)
    assert(getWordScore("jo", 7) == 9)

def test_bonus():
    assert(getWordScore("muzjiks", 7) == 79)
