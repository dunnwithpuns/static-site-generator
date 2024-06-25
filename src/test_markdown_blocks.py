import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_type_heading,
    block_type_code,
    block_type_ol,
    block_type_paragraph,
    block_type_quote,
    block_to_block_type,
    block_type_ul,
    paragraph_to_html_node,
    markdown_to_html_node,
)

from htmlnode import(
    HTMLNode,
    ParentNode,
    LeafNode,
)

class testBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "       This is **bolded** paragraph\n\n       This is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line\n\n* This is a list\n* with items "
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here \nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_markdown_to_blocks2(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_block_to_block_type_paragraph(self):
        block = "This is a pargraph block."
        expected = block_type_paragraph
        self.assertEqual(block_to_block_type(block), expected)

    def test_paragraph_to_html(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_heading(self):
        md = """
# This is a main page header

## This is a secondary header

### This is a tertiary header

#### This is fourth degree header

This is paragraph text

###### This is a sixth degree header 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a main page header</h1><h2>This is a secondary header</h2><h3>This is a tertiary header</h3><h4>This is fourth degree header</h4><p>This is paragraph text</p><h6>This is a sixth degree header</h6></div>"
        )

    def test_blockquote(self):
        md = """
> Line one of the quote 
> Line two of the quote

Seperate paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Line one of the quote Line two of the quote</blockquote><p>Seperate paragraph</p></div>"
        )
    def test_code(self):
        md = """
```
a, b = 0, 1
while b < 10:
    print(b)
    a, b = a, a + b
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><pre><code>a, b = 0, 1\nwhile b < 10:\n    print(b)\n    a, b = a, a + b\n</code></pre></div>"""
        )

if __name__ == "__main__":
    unittest.main()