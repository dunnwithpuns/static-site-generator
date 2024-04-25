import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_args(self):
        node = HTMLNode("p", "this is value text", "<p>", {"href": "https://www.google.com"})
        expected_repr = """HTMLNode(tag=p, value=this is value text, children=<p>, props=href=https://www.google.com)"""
        self.assertEqual(repr(node), expected_repr)

    def test_tag(self):
        node = HTMLNode(value="this is value text", children="<p>", props={"href": "https://www.google.com"})
        expected_repr = """HTMLNode(tag=None, value=this is value text, children=<p>, props=href=https://www.google.com)""" 
        self.assertEqual(repr(node), expected_repr)

    def test_children(self):
        node = HTMLNode(tag="p", value="this is value text", props={"href": "https://www.google.com"})
        expected_repr = """HTMLNode(tag=p, value=this is value text, children=None, props=href=https://www.google.com)"""
        self.assertEqual(repr(node), expected_repr)

    def test_props(self):
        node = HTMLNode("p", "this is value text", "<p>")
        expected_repr = """HTMLNode(tag=p, value=this is value text, children=<p>, props=None)"""
        self.assertEqual(repr(node), expected_repr)
     
if __name__ == '__main__':
    unittest.main()