from htmlnode import(
    HTMLNode,
    ParentNode,
    LeafNode,
)

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
    return 

def block_to_block_type(block):
    if block.startswith(">"):
        return block_type_quote
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code   
    if block.startswith("1. "):
        lines = block.split("\n") 
        i = 1
        for line in lines:
            if not line.startswith("{i}. "):
                return block_type_ordered_list
            i += 1
    elif block.startswith("* ") or block.startswith("- "):
        return block_type_unordered_list
    else:
        return block_type_paragraph