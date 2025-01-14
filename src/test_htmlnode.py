import unittest

from htmlnode import *

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    


    def test_nodes_with_same_properties_are_equal(self):
        node = HTMLNode("a", "toto",[],props)
        node.props_to_html()

    def test_nodes_with_same_properties_are_equal(self):
        node = HTMLNode("a", "toto",[],props)
        node.props_to_html()
        print (node.props_to_html())
        print(node)


if __name__ == "__main__":
    unittest.main()