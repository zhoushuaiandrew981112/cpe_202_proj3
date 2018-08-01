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









if __name__ == "__main__":
    unittest.main()
