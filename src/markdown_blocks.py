from htmlnode import(
    HTMLNode,
    ParentNode,
    LeafNode,
)
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block) 
    return filtered_blocks 

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
        nodes.append(html_node)
    return ParentNode("div", nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html(block)
    if block_type == block_type_code:
        return code_to_html(block)
    if block_type == block_type_quote:
        return quote_to_html(block)
    if block_type == block_type_unordered_list:
        return unordered_to_html(block)
    if block_type == block_type_ordered_list:
        return ordered_to_html(block)
    raise ValueError("Invalid block type")

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph 
        return block_type_quote
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code   
    if block.startswith("1. "): 
        i = 1
        for line in lines:
            if not line.startswith("{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list 
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list 
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list 
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html(block, type):
    if type != block_type_paragraph:
        raise ValueError("Invalid block type")
    return HTMLNode("p", block)

def code_to_html(block, type):
    if type != block_type_code:
        raise ValueError("Invalid block type")
    return ParentNode("pre", LeafNode("code", block))

def quote_to_html(block, type):
    if type != block_type_quote:
        raise ValueError("Invalid block type")
    return HTMLNode("blockquote", block)

def unordered_to_html(block, type):
    if type != block_type_unordered_list:
        raise ValueError("Invalid block type")
    return ParentNode("li", LeafNode("ul", block))

def ordered_to_html(block, type):
    if type != block_type_ordered_list:
        raise ValueError("Invalid block type")
    return ParentNode("li", LeafNode("ol", block))

def heading_to_html(block, type=block_type_heading):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalide heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

