import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
)

def process_split_nodes_image(old_node, image_tups):     
    split_nodes = [] 
    text = old_node.text
    for image in image_tups: 
        sections = text.split(f"![{image[0]}]({image[1]})", 1)
        for i, sect in enumerate(sections):
            if sect == "":
                continue 
            if i == 1:
                split_nodes.append(TextNode(image[0], text_type_image, image[1]))
            split_nodes.append(TextNode(sect, text_type_text))
        text = sections[1]
    return split_nodes

# split image nodes
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
           new_nodes.append(old_node)
           continue
        image_tups = extract_md_images(old_node.text)
        if not image_tups:
            return old_node   
        new_nodes.extend(process_split_nodes_image(old_node, image_tups))
    return new_nodes 

# function processing split nodes 
def process_split_nodes_delimiter(old_node, delimiter, text_type):
    sections = old_node.text.split(delimiter) 
    split_nodes = []
    if len(sections) % 2 == 0:
        raise ValueError(f"Invalid markdown, {delimiter} section not closed")
    for i, sect in enumerate(sections):
        if sect == "":
            continue
        if i % 2 == 0:
            split_nodes.append(TextNode(sect, text_type_text))
        else: 
            split_nodes.append(TextNode(sect, text_type))
    
    return split_nodes

# splitting nodes based on their delimiter
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        new_nodes.extend(process_split_nodes_delimiter(old_node, delimiter, text_type))
    return new_nodes 

def extract_md_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_md_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches