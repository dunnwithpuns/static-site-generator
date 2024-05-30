from markdown_blocks import (
    block_to_block_type,
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered_list,
    markdown_to_blocks,
)

from htmlnode import (
    HTMLNode,
    ParentNode,
    LeafNode,
)

def paragraph_to_html(block, type=block_type_paragraph):
    return HTMLNode("p", block)

def code_to_html(block, type=block_type_code):
    return ParentNode("pre", LeafNode("code", block))

def quote_to_html(block, type=block_type_quote):
    return HTMLNode("blockquote", block)

def unordered_to_html(block, type=block_type_unordered_list):
    return ParentNode("li", LeafNode("ul", block))

def ordered_to_html(block, type=block_type_ordered_list):
    return ParentNode("li", LeafNode("ol", block))

def heading_to_html(block, type=block_type_heading):
    return 