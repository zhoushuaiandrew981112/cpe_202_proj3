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

    
    def __lt__(self, other):
        return comes_before(self, other)


def get_char_freq(string):
    length = 256
    freq_lst = [0] * length
    for char in string:
        freq_lst[ord(char)] += 1
    return freq_lst


def comes_before(tree_a, tree_b):
    if tree_a.freq == tree_b.freq:
        #return ord(tree_a.char) < ord(tree_b.char)
        return tree_a.char < tree_b.char
    return tree_a.freq < tree_b.freq


def sort_node_lst(node_lst):
    for i in range(1, len(node_lst)):
        key = node_lst[i]
        j = i - 1
        while j >= 0 and (key.freq < node_lst[j].freq or key.freq == \
            node_lst[j].freq and ord(key.char) < ord(node_lst[j].char)):
            node_lst[j + 1] = node_lst[j]
            j -= 1
        node_lst[j + 1] = key


def display(node_lst):
    for node in node_lst:
        print(node.char, node.freq, end = " | ")
    print("")


def combine_nodes(tree_a, tree_b):
    freq_sum = tree_a.freq + tree_b.freq 
    if ord(tree_a.char) < ord(tree_b.char):
        return HuffmanNode(tree_a.char, freq_sum, tree_a, tree_b)
    else:
        return HuffmanNode(tree_b.char, freq_sum, tree_a, tree_b)


def create_tree(freq_lst):
    node_lst = []
    for freq in range(0, len(freq_lst)):
        if freq_lst[freq] > 0:
            n = HuffmanNode(chr(freq), freq_lst[freq])
            node_lst.append(n)
    node_lst.sort()
    if len(node_lst) == 0:
        return None
    elif len(node_lst) == 1:
        return node_lst[0] 
    while len(node_lst) >= 2:
        tree_a = node_lst.pop(0)
        tree_b = node_lst.pop(0)
        node_lst.append(combine_nodes(tree_a, tree_b))
        node_lst.sort()
    return node_lst[0]


def code_gen(code, node, code_lst):
    if not (node.l_child == None and node.r_child == None):
        code_gen(code + "0", node.l_child, code_lst)
        code_gen(code + "1", node.r_child, code_lst)
    else:
        code_lst[ord(node.char)] = code


def create_code(root):
    lst_len = 256
    code_lst = [""] * lst_len
    if root == None:
        return code_lst
    code_gen("", root, code_lst)
    return code_lst 


def encode(string):
    code_lst = create_code(create_tree(get_char_freq(string)))
    code_str = ""
    for char in string:
        code_str += code_lst[ord(char)]
    return code_str


def decode(string, freq_lst):
    og_str = ""
    tree = create_tree(freq_lst)
    current = tree
    for letter in string:
        if letter == "0":
            current = current.l_child
            if current.l_child == None and current.r_child == None:
                og_str += current.char
                current = tree
        elif letter == "1":
            current = current.r_child
            if current.l_child == None and current.r_child == None:
                og_str += current.char
                current = tree
    return og_str







