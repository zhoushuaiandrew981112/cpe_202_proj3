from alphabits import *
import unittest


class Test_proj3(unittest.TestCase):

    def test_HuffmanNode(self):
        n = HuffmanNode("0", 1)
        self.assertEqual(n.char, "0")
        self.assertEqual(n.freq, 1)
        self.assertEqual(n.l_child, None)
        self.assertEqual(n.r_child, None)

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


    def test_create_tree_lst(self):
        string = "abcd abc ab a"
        freq_lst = get_char_freq(string)
        act_tree = create_tree(freq_lst)

        node_d_1 = HuffmanNode("d", 1)
        node_c_2 = HuffmanNode("c", 2)
        node_c_3 = HuffmanNode("c", 3, node_d_1, node_c_2)
        node_a_4 = HuffmanNode("a", 4)
        node_a_7 = HuffmanNode("a", 7)
        node_b_3 = HuffmanNode("b", 3)
        node_space_3 = HuffmanNode(" ", 3)
        node_space_6 = HuffmanNode(" ", 6)
        node_space_13 = HuffmanNode(" ", 13)





if __name__ == "__main__":
    unittest.main()
