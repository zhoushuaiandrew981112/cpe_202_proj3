# Name:         Zhoushuai (Andrew) Wu
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Proj 3: Alphabits
# Term:         Summer 2018


class HuffmanNode:
    
    def __init__(self, char, freq, l_child = None, r_child = None):
        self.char = char
        self.freq = freq
        self.l_child = l_child
        self.r_child = r_child


def get_char_freq(string):
    length = 256
    freq_lst = [0] * length
    for char in string:
        freq_lst[ord(char)] += 1
    return freq_lst


def comes_before(tree_a, tree_b):
    if tree_a.freq < tree_b.freq:
        return True
    elif tree_a.freq > tree_b.freq:
        return False
    elif tree_a.freq == tree_b.freq:
        if ord(tree_a.char) < ord(tree_b.char):
            return True
        elif ord(tree_a.char) > ord(tree_b.char):
            return False







