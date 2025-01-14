import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
  

    def test_nodes_with_same_properties_are_equal(self):
        node = TextNode("This is a text node", TextType.BOLD,"goog.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"goog.com")
        self.assertEqual(node, node2)

    def test_nodes_with_different_properties_are_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD ,"goog.com")
        node3 = TextNode("This is a text node", TextType.ITALIC, "toto.com")
        self.assertNotEqual(node, node3)

    def test_nodes_with_blank_text_and_url_are_equal(self):
        node4 = TextNode("", TextType.ITALIC, "None")
        node5 = TextNode("", TextType.ITALIC, "None")
        self.assertEqual(node4, node5)
        
if __name__ == "__main__":
    unittest.main()