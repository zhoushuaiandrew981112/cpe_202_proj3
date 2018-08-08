from alphabits import *
import unittest


class Test_proj3(unittest.TestCase):

    def test_HuffmanNode(self):
        n = HuffmanNode("0", 1)
        self.assertEqual(n.char, "0")
        self.assertEqual(n.freq, 1)
        self.assertEqual(n.l_child, None)
        self.assertEqual(n.r_child, None)

    def testHuffmanNode__lt__(self):
        n_0 = HuffmanNode("0", 0)
        n_1 = HuffmanNode("1", 1)
        n_2 = HuffmanNode("2", 2)
        n_3 = HuffmanNode("3", 3)
        n_4 = HuffmanNode("4", 4)
        n_5 = HuffmanNode("5", 5)
        self.assertTrue(n_0 < n_1)
        self.assertTrue(n_1 > n_0)
        self.assertTrue(n_2 < n_3)
        self.assertTrue(n_3 > n_2)
        self.assertTrue(n_4 < n_5)
        self.assertTrue(n_5 > n_4)

    def test_get_char_freq_0(self):
        string = "hello"
        freq_lst = get_char_freq(string)
        self.assertEqual(freq_lst[ord("h")], 1)
        self.assertEqual(freq_lst[ord("e")], 1)
        self.assertEqual(freq_lst[ord("l")], 2)
        self.assertEqual(freq_lst[ord("o")], 1)
       
    def test_get_char_freq_1(self):
        string = "!@#$"
        freq_lst = get_char_freq(string)
        self.assertEqual(freq_lst[ord("!")], 1)
        self.assertEqual(freq_lst[ord("@")], 1)
        self.assertEqual(freq_lst[ord("#")], 1)
        self.assertEqual(freq_lst[ord("$")], 1)
       
    def test_get_char_freq_2(self):
       
        string = "abcd abc ab a"
        freq_lst = get_char_freq(string)
        self.assertEqual(freq_lst[ord("a")], 4)
        self.assertEqual(freq_lst[ord("b")], 3)
        self.assertEqual(freq_lst[ord("c")], 2)
        self.assertEqual(freq_lst[ord("d")], 1)
        self.assertEqual(freq_lst[ord(" ")], 3)

    def test_comes_before(self):
        tree_a = HuffmanNode("a", 0)
        tree_b = HuffmanNode("b", 1)
        
        self.assertTrue(comes_before(tree_a, tree_b))
        self.assertFalse(comes_before(tree_b, tree_a))
        
        tree_b = HuffmanNode("b", 0)
        
        self.assertTrue(comes_before(tree_a, tree_b))
        self.assertFalse(comes_before(tree_b, tree_a))

    def test_sort_node_lst(self):
        node_0 = HuffmanNode("0", 1)
        node_1 = HuffmanNode("1", 1)
        node_2 = HuffmanNode("2", 2)
        node_3 = HuffmanNode("3", 3)
        node_4 = HuffmanNode("4", 4)
        node_5 = HuffmanNode("5", 4)

        node_lst = [node_2, node_5, node_4, node_0, node_3, node_1]

        sort_node_lst(node_lst)
        
        self.assertEqual(node_lst[0].freq, 1)
        self.assertEqual(node_lst[1].freq, 1)
        self.assertEqual(node_lst[2].freq, 2)
        self.assertEqual(node_lst[3].freq, 3)
        self.assertEqual(node_lst[4].freq, 4)
        self.assertEqual(node_lst[5].freq, 4)


        string = "abcd abc ab a"
        freq_lst = get_char_freq(string)

        node_lst = []
        for freq in range(0, len(freq_lst)):
            if freq_lst[freq] != 0:
                n = HuffmanNode(chr(freq), freq_lst[freq])
                node_lst.append(n)

        sort_node_lst(node_lst)

        self.assertEqual(node_lst[0].freq, 1)
        self.assertEqual(node_lst[0].char, "d")
        self.assertEqual(node_lst[1].freq, 2)
        self.assertEqual(node_lst[1].char, "c")
        self.assertEqual(node_lst[2].freq, 3)
        self.assertEqual(node_lst[2].char, " ")
        self.assertEqual(node_lst[3].freq, 3)
        self.assertEqual(node_lst[3].char, "b")
        self.assertEqual(node_lst[4].freq, 4)
        self.assertEqual(node_lst[4].char, "a")

    def test_combine_nodes(self):

        node_a_2 = HuffmanNode("a", 2)
        node_b_2 = HuffmanNode("b", 2)
        node_c_2 = HuffmanNode("c", 2)
        node_a_4 = HuffmanNode("a", 4, node_a_2, node_b_2)
        node_b_4 = HuffmanNode("b", 4, node_b_2, node_c_2)
 
        new_node = combine_nodes(node_a_2, node_b_2)
        self.assertEqual(new_node.freq, node_a_4.freq)
        self.assertEqual(new_node.char, node_a_4.char)

        new_node = combine_nodes(node_b_2, node_c_2)
        self.assertEqual(new_node.freq, node_b_4.freq)
        self.assertEqual(new_node.char, node_b_4.char)

        new_node = combine_nodes(node_a_2, node_b_2)
        self.assertEqual(new_node.freq, node_a_4.freq)
        self.assertEqual(new_node.char, node_a_4.char)

        new_node = combine_nodes(node_b_2, node_c_2)
        self.assertEqual(new_node.freq, node_b_4.freq)
        self.assertEqual(new_node.char, node_b_4.char)

    def test_create_tree_lst(self):
        string = " "
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        self.assertEqual(act_tree.freq, 1)
        self.assertEqual(act_tree.char, " ")
        

        string = "abcd abc ab a"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)

        node_d_1 = HuffmanNode("d", 1)
        node_c_2 = HuffmanNode("c", 2)
        node_c_3 = HuffmanNode("c", 3, node_d_1, node_c_2)
        node_a_4 = HuffmanNode("a", 4)
        node_a_7 = HuffmanNode("a", 7, node_c_3, node_a_4)
        node_b_3 = HuffmanNode("b", 3)
        node_space_3 = HuffmanNode(" ", 3)
        node_space_6 = HuffmanNode(" ", 6, node_space_3, node_b_3)
        node_space_13 = HuffmanNode(" ", 13, node_space_6, node_a_7)


        act_node_space_13 = act_tree 
        act_node_space_6 = act_node_space_13.l_child 
        act_node_a_7 = act_node_space_13.r_child
        act_node_space_3 = act_node_space_6.l_child
        act_node_b_3 = act_node_space_6.r_child 
        act_node_c_3 = act_node_a_7.l_child 
        act_node_a_4 = act_node_a_7.r_child
        act_node_d_1 = act_node_c_3.l_child 
        act_node_c_2 = act_node_c_3.r_child
        
        self.assertEqual(act_node_space_13.freq, node_space_13.freq)
        self.assertEqual(act_node_space_13.char, node_space_13.char)
        self.assertEqual(act_node_space_13.l_child.freq, node_space_6.freq)
        self.assertEqual(act_node_space_13.l_child.char, node_space_6.char)
        self.assertEqual(act_node_space_13.r_child.freq, node_a_7.freq)
        self.assertEqual(act_node_space_13.r_child.char, node_a_7.char)
        
        self.assertEqual(act_node_space_6.freq, node_space_6.freq)
        self.assertEqual(act_node_space_6.char, node_space_6.char)
        self.assertEqual(act_node_space_6.l_child.freq, node_space_3.freq)
        self.assertEqual(act_node_space_6.l_child.char, node_space_3.char)
        self.assertEqual(act_node_space_6.r_child.freq, node_b_3.freq)
        self.assertEqual(act_node_space_6.r_child.char, node_b_3.char)

        self.assertEqual(act_node_a_7.freq, node_a_7.freq)
        self.assertEqual(act_node_a_7.char, node_a_7.char)
        self.assertEqual(act_node_a_7.l_child.freq, node_c_3.freq)
        self.assertEqual(act_node_a_7.l_child.char, node_c_3.char)
        self.assertEqual(act_node_a_7.r_child.freq, node_a_4.freq)
        self.assertEqual(act_node_a_7.r_child.char, node_a_4.char)

        self.assertEqual(act_node_b_3.freq, node_b_3.freq)
        self.assertEqual(act_node_b_3.char, node_b_3.char)
        self.assertEqual(act_node_b_3.l_child, None)
        self.assertEqual(act_node_b_3.r_child, None)

        self.assertEqual(act_node_space_3.freq, node_space_3.freq)
        self.assertEqual(act_node_space_3.char, node_space_3.char)
        self.assertEqual(act_node_space_3.l_child, None)
        self.assertEqual(act_node_space_3.r_child, None)

        self.assertEqual(act_node_c_3.freq, node_c_3.freq)
        self.assertEqual(act_node_c_3.char, node_c_3.char)
        self.assertEqual(act_node_c_3.l_child.freq, node_d_1.freq)
        self.assertEqual(act_node_c_3.l_child.char, node_d_1.char)
        self.assertEqual(act_node_c_3.r_child.freq, node_c_2.freq)
        self.assertEqual(act_node_c_3.r_child.char, node_c_2.char)

        self.assertEqual(act_node_a_4.freq, node_a_4.freq)
        self.assertEqual(act_node_a_4.char, node_a_4.char)
        self.assertEqual(act_node_a_4.l_child, None)
        self.assertEqual(act_node_a_4.r_child, None)

        self.assertEqual(act_node_d_1.freq, node_d_1.freq)
        self.assertEqual(act_node_d_1.char, node_d_1.char)
        self.assertEqual(act_node_d_1.l_child, None)
        self.assertEqual(act_node_d_1.r_child, None)

        self.assertEqual(act_node_c_2.freq, node_c_2.freq)
        self.assertEqual(act_node_c_2.char, node_c_2.char)
        self.assertEqual(act_node_c_2.l_child, None)
        self.assertEqual(act_node_c_2.r_child, None)

        string = "hello prof kauffma"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        self.assertEqual(act_tree.freq, 18)
        self.assertEqual(act_tree.char, " ")

        string = "hello coco"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        self.assertEqual(act_tree.freq, 10)
        self.assertEqual(act_tree.char, " ")

        string = "hello marisa"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        self.assertEqual(act_tree.freq, 12)
        self.assertEqual(act_tree.char, " ")

        string = "hello joice"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        self.assertEqual(act_tree.freq, 11)
        self.assertEqual(act_tree.char, " ")

        freq_lst = [0] * 256
        act_tree = create_tree(freq_lst)
        

        string = "xx yyy zzz"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)

        node_space_2 = HuffmanNode(" ", 2)
        node_z_2 = HuffmanNode("z", 2)
        node_space_4 = HuffmanNode(" ", 4, node_space_2, node_z_2)
        node_y_3 = HuffmanNode("y", 3)
        node_z_3 = HuffmanNode("z", 3)
        node_y_6 = HuffmanNode("y", 6, node_y_3, node_z_3)
        node_space_10 = HuffmanNode(" ", 10, node_space_4, node_y_6)

        self.assertEqual(act_tree.freq, node_space_10.freq)
        self.assertEqual(act_tree.char, node_space_10.char)

        string = "abbcccddddeeeeeffffff"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)


    def test_create_code(self):
        
        exp_code_lst = [""] * 256

        act_code_lst = create_code(None)
        self.assertEqual(act_code_lst, exp_code_lst)

        string = "abcd abc ab a"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        act_code_lst = create_code(act_tree)
        
        exp_code_lst = [""] * 256
        exp_code_lst[ord(" ")] = "00"
        exp_code_lst[ord("a")] = "11"
        exp_code_lst[ord("b")] = "01"
        exp_code_lst[ord("c")] = "101"
        exp_code_lst[ord("d")] = "100"

        self.assertEqual(act_code_lst, exp_code_lst)


        string = "hello prof kauffma"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        act_code_lst = create_code(act_tree)

        exp_code_lst = [""] * 256
        exp_code_lst[ord(" ")] = "1101"       
        exp_code_lst[ord("a")] = "000"       
        exp_code_lst[ord("e")] = "0010"       
        exp_code_lst[ord("f")] = "111"       
        exp_code_lst[ord("h")] = "0011"       
        exp_code_lst[ord("k")] = "0100"       
        exp_code_lst[ord("l")] = "011"       
        exp_code_lst[ord("m")] = "0101"       
        exp_code_lst[ord("o")] = "100"       
        exp_code_lst[ord("p")] = "1010"       
        exp_code_lst[ord("r")] = "1011"       
        exp_code_lst[ord("u")] = "1100"       

        string = "hello coco"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        act_code_lst = create_code(act_tree)

        exp_code_lst = [""] * 256
        exp_code_lst[ord(" ")] = "1010"
        exp_code_lst[ord("c")] = "00"
        exp_code_lst[ord("e")] = "1011"
        exp_code_lst[ord("h")] = "100"
        exp_code_lst[ord("l")] = "01"
        exp_code_lst[ord("o")] = "11"

        string = "hello marisa"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        act_code_lst = create_code(act_tree)

        exp_code_lst = [""] * 256
        exp_code_lst[ord(" ")] = "000"
        exp_code_lst[ord("a")] = "101"
        exp_code_lst[ord("e")] = "1001"
        exp_code_lst[ord("h")] = "1100"
        exp_code_lst[ord("i")] = "1101"
        exp_code_lst[ord("l")] = "111"
        exp_code_lst[ord("m")] = "000"
        exp_code_lst[ord("o")] = "001"
        exp_code_lst[ord("r")] = "010"
        exp_code_lst[ord("s")] = "011"

        string = "hello joice"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)
        act_code_lst = create_code(act_tree)

        exp_code_lst = [""] * 256
        exp_code_lst[ord(" ")] = "1010"
        exp_code_lst[ord("c")] = "1011"
        exp_code_lst[ord("e")] = "110"
        exp_code_lst[ord("h")] = "1110"
        exp_code_lst[ord("i")] = "111"
        exp_code_lst[ord("j")] = "100"
        exp_code_lst[ord("l")] = "00"
        exp_code_lst[ord("o")] = "01"


    def test_encode(self):

        string = "abcd abc ab a"
        exp_code_str = "11011011000011011010011010011"
        act_code_str = encode(string)
        self.assertEqual(act_code_str, exp_code_str)

        string = "hello prof kauffma"
        act_code_str = encode(string)
        exp_code_str = "001100100110111001101101010111001111101010000011001111110101000"
        self.assertEqual(act_code_str, exp_code_str)

        string = "hello coco"
        act_code_str = encode(string)
        exp_code_str = "1001011010111101000110011"
        self.assertEqual(act_code_str, exp_code_str)

        string = "hello marisa"
        act_code_str = encode(string)
        exp_code_str = "1100100111111100110000001010101101011101"
        self.assertEqual(act_code_str, exp_code_str)

        string = "hello joice"
        act_code_str = encode(string)
        exp_code_str = "111011000000110101000111111011110"
        self.assertEqual(act_code_str, exp_code_str)


    def test_decode(self):
        string = "abcd abc ab a"
        code_str = "11011011000011011010011010011"
        freq_lst = get_char_freq(string)
        act_string = decode(code_str, freq_lst)

        self.assertEqual(act_string, string)

        string = "abcd abc ab a"
        code_str = "11011011000011011010011010011"
        freq_lst = get_char_freq(string)
        act_string = decode(code_str, freq_lst)

        self.assertEqual(act_string, string)

        string = "hello coco"
        code_str = "1001011010111101000110011"
        freq_lst = get_char_freq(string)
        act_string = decode(code_str, freq_lst)

        self.assertEqual(act_string, string)

        string = "hello marisa"
        code_str = "1100100111111100110000001010101101011101"
        freq_lst = get_char_freq(string)
        act_string = decode(code_str, freq_lst)

        self.assertEqual(act_string, string)

        string = "hello joice"
        code_str = "111011000000110101000111111011110"
        freq_lst = get_char_freq(string)
        act_string = decode(code_str, freq_lst)
        
        self.assertEqual(act_string, string)

        

if __name__ == "__main__":
    unittest.main()
