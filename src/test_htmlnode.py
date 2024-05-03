import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_args(self):
        node = HTMLNode("p", "this is value text", "<p>", {"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(p, this is value text, <p>, href="https://www.google.com" target="_blank")"""
        self.assertEqual(repr(node), expected_repr)

    def test_tag(self):
        node = HTMLNode(value="this is value text", children="<p>", props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(None, this is value text, <p>, href="https://www.google.com" target="_blank")""" 
        self.assertEqual(repr(node), expected_repr)

    def test_value(self):
        node = HTMLNode(tag="h", children="<p>", props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(h, value=None, <p>, href="https://www.google.com" target="_blank")"""
        self.assertEqual(repr(node), expected_repr)

    def test_children(self):
        node = HTMLNode(tag="p", value="this is value text", props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = """HTMLNode(p, this is value text, children=None, href="https://www.google.com" target="_blank")"""
        self.assertEqual(repr(node), expected_repr)

    def test_props(self):
        node = HTMLNode("p", "this is value text", "<p>")
        expected_repr = """HTMLNode(p, this is value text, <p>, props=None)"""
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_to_html1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_valueless(self):
        node = LeafNode(tag="h", props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_ParentNode_Nest(self):
        node = ParentNode(
            "h",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
            ]
        )
        expected = "<h><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></h>"
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode_children(self):
        node = ParentNode(
            "h",[]
        )
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_ParentNode_children1(self):
        node = ParentNode(
            "h", None
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_ParentNode_ComplexNesting(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        ParentNode(
                            "li",
                            [LeafNode(None, "Item 1")],
                        ),
                        ParentNode(
                            "li",
                            [LeafNode(None, "Item 2"),
                            ParentNode(
                                "ul",
                                [LeafNode("li", "Subitem 1"),
                                LeafNode("li", "Subitem 2")]
                            )]
                        ),
                    ]
                )
            ]
        )
        expected = "<div><ul><li>Item 1</li><li>Item 2<ul><li>Subitem 1</li><li>Subitem 2</li></ul></li></ul></div>"
        self.assertEqual(node.to_html(), expected)

if __name__ == '__main__':
    unittest.main()