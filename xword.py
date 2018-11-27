#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "???"

# YOUR HELPER FUNCTION GOES HERE
import re


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    pattern = r'[a-z]'
    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
        
    replace_word = test_word.replace(' ',pattern)
    

    for word in words:
        if re.search(replace_word, word):
            if len(test_word) == len(word):
                print word
           
if __name__ == '__main__':
    main()
