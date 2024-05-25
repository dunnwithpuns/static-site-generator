
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

def block_to_block_type(block):
    list_items = block.split("\n")
    if block.startswith(">"):
        return block_type_quote
    elif block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    elif block.startswith("* ") or block.startswith("- "):
        return block_type_unordered_list
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code  
    elif block[0].isdigit() and block[1:2] == ". ":
        return block_type_ordered_list
    else:
        return block_type_paragraph