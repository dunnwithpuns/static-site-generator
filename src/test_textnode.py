import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
