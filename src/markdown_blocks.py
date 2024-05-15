
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.splitlines()
    while "" in blocks:
        blocks.remove("")
    blocks = [block.strip() for block in blocks]
    return blocks 

def block_to_block_type(block):
    if block[0] == ">":
        return block_type_quote
    elif block[0:1] == "* " or block[0:1] == "- ":
        return block_type_unordered_list
    else:
        return block_type_paragraph