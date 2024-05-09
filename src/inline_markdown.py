import re

from textnode import (
    TextNode,
    text_type_text,
)

def process_split_nodes(old_node, delimiter, text_type):
    sections = old_node.text.split(delimiter) 
    split_nodes = []
    if len(sections) % 2 == 0:
        raise ValueError("Invalid markdown, formatted section not closed")
    for i, sect in enumerate(sections):
        if sect == "":
            continue
        if i % 2 == 0:
            split_nodes.append(TextNode(sect, text_type_text))
        else: 
            split_nodes.append(TextNode(sect, text_type))
    
    return split_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        split_nodes = process_split_nodes(old_node, delimiter, text_type)
        new_nodes.extend(split_nodes)
    return new_nodes 

def extract_md_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_md_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches