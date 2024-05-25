import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_to_block_type,
    block_type_unordered_list,
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

    def test_block_to_block_type_heading(self):
        block = "## This is a Secondary Heading block."
        expected = block_type_heading
        self.assertEqual(block_to_block_type(block), expected)
    
    def test_block_to_block_type_quote(self):
        block = ">This is a quote block"
        expected = block_type_quote
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_ul(self):
        block = "*This is an unordered list block\n*This is another item in the list"
        expected = block_type_unordered_list
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_code(self):
        block = "```\nThis is a code block\n```"
        expected = block_type_code
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_ol(self):
        block = "1. This is an ordered list block\n2. This is another item in the ordered list"
        expected = block_type_ordered_list
        self.assertEqual(block_to_block_type(block), expected)

if __name__ == "__main__":
    unittest.main()