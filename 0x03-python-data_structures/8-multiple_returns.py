#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        res1 = len(sentence)
        res2 = None
        res = res1, res2
        return res
    res1 = len(sentence)
    res2 = sentence[0]
    res = res1, res2
    return res
