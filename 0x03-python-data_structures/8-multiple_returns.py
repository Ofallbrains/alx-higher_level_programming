#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = None
    if sentence:
        first_char = sentence[0]
    len_sentence = len(sentence)
    return (len_sentence, first_char)
