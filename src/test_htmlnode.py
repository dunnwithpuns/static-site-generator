import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_args(self):
        node = HTMLNode("p", "this is value text", "<p>", {"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(tag=p, value=this is value text, children=<p>, props= href="https://www.google.com" target="_blank")"""
        self.assertEqual(repr(node), expected_repr)

    def test_tag(self):
        node = HTMLNode(value="this is value text", children="<p>", props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(tag=None, value=this is value text, children=<p>, props= href="https://www.google.com" target="_blank")""" 
        self.assertEqual(repr(node), expected_repr)

    def test_value(self):
        node = HTMLNode(tag="h", children="<p>", props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(tag=h, value=None, children=<p>, props= href="https://www.google.com" target="_blank")"""
        self.assertEqual(repr(node), expected_repr)

    def test_children(self):
        node = HTMLNode(tag="p", value="this is value text", props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(tag=p, value=this is value text, children=None, props= href="https://www.google.com" target="_blank")"""
        self.assertEqual(repr(node), expected_repr)

    def test_props(self):
        node = HTMLNode("p", "this is value text", "<p>")
        expected_repr = """HTMLNode(tag=p, value=this is value text, children=<p>, props=None)"""
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_to_html1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_valueless(self):
        node = LeafNode(tag="h", props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()
    
if __name__ == '__main__':
    unittest.main()