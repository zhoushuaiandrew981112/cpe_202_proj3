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


def sort_node_lst(node_lst):
    for i in range(1, len(node_lst)):
        key = node_lst[i]
        j = i - 1
        while j >= 0 and (key.freq < node_lst[j].freq or key.freq == node_lst[j].freq \
            and ord(key.char) < ord(node_lst[j].char)):
            node_lst[j + 1] = node_lst[j]
            j -= 1
        node_lst[j + 1] = key


def create_tree(freq_lst):
    node_lst = []
    for char in freq_lst:
        if char != 0:
            node_lst.append(HuffmanNode(chr(freq_lst.index(char)), char))
    sort_node_lst(node_lst)
    while len(node_lst) > 2:
        tree_a = node_lst.pop(0)
        tree_b = node_lst.pop(1)
        if comes_before(tree_a, tree_b):
            freq_sum = tree_a.freq + tree_b.freq
            new_node = HuffmanNode(tree_a.char, freq_sum, tree_a, tree_b)
        else:
            freq_sum = tree_a.freq + tree_b.freq
            new_node = HuffmanNode(tree_b.char, freq_sum, tree_b, tree_a)
        node_lst.append(new_node)
        sort_node_lst(node_lst)
    return node_lst[0]






