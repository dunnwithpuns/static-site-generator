import unittest

from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)
from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("Text node test", text_type_italic, "https://www.boot.dev/")
        node1 = TextNode("Text node test", text_type_italic, "https://www.boot.dev/")
        self.assertEqual(node, node1)

    def test_not_eq(self):
        node = TextNode("Text node test", text_type_italic)
        node1 = TextNode("Text node test", text_type_bold)
        self.assertNotEqual(node, node1)

    def test_not_eq1(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev/")
        node1 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node1)
    
    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_to_html_link(self):
        node = text_node_to_html_node(TextNode("Check out this website!", text_type_link, "https://www.google.com"))
        expected = LeafNode("a", "Check out this website!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), expected.to_html())
    
    def test_text_to_html_text(self):
        node = text_node_to_html_node(TextNode("This is a text node", text_type_bold))
        expected = LeafNode("b", "This is a text node")
        self.assertEqual(node.to_html(), expected.to_html())

    def test_text_to_html_img(self):
        node = text_node_to_html_node(TextNode("This is an image link", text_type_image, "https://www.google.com"))
        expected = LeafNode("img", value="", props={"src": "https://www.google.com", "alt": "This is an image link"})
        self.assertEqual(node.to_html(), expected.to_html())
    
   
if __name__ == "__main__":
    unittest.main()
