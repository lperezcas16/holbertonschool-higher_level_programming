#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    size = len(sentence)
    if size > 0:
        first = sentence[0]
    return size, first
