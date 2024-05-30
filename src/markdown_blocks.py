
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