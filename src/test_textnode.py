import unittest

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("Text node test", "italic", "https://www.boot.dev/")
        node1 = TextNode("Text node test", "italic", "https://www.boot.dev/")
        self.assertEqual(node, node1)

    def test_not_eq(self):
        node = TextNode("Text node test", "italic")
        node1 = TextNode("Text node test", "bold")
        self.assertNotEqual(node, node1)

    def test_not_eq1(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev/")
        node1 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node1)

    def test_text_to_html_link(self):
        node = TextNode("Check out this website!", "link", "https://www.google.com").text_node_to_html_node()
        expected = LeafNode("a", "Check out this website!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), expected.to_html())
    
    def test_text_to_html_text(self):
        node = TextNode("This is a text node", "bold").text_node_to_html_node()
        expected = LeafNode("b", "This is a text node")
        self.assertEqual(node.to_html(), expected.to_html())

    def test_text_to_html_img(self):
        node = TextNode("This is an image link", "image", "https://www.google.com").text_node_to_html_node()
        expected = LeafNode("img", value="", props={"scr": "https://www.google.com", "alt": "This is an image link"})
        self.assertEqual(node.to_html(), expected.to_html())

if __name__ == "__main__":
    unittest.main()
