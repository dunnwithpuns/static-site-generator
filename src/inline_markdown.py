import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_code,
    text_type_bold,
    text_type_italic,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)] 
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes 

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        new_nodes.extend(process_split_nodes_delimiter(old_node, delimiter, text_type))
    return new_nodes 

def process_split_nodes_link(old_node, links):
    split_nodes = []
    text = old_node.text
    for link in links:
        sections = text.split(f"[{link[0]}]({link[1]})", 1)
        if len(sections) != 2:
            raise ValueError("Invalid markdown, link section not closed") 
        if sections[0] != "":
            split_nodes.append(TextNode(sections[0], text_type_text))
        split_nodes.append(TextNode(link[0], text_type_link, link[1]))
        text = sections[1]
    if text.strip():
        split_nodes.append(TextNode(text, text_type_text))
    return split_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links = extract_md_links(old_node.text)
        if not links:
           new_nodes.append(old_node)
           continue
        new_nodes.extend(process_split_nodes_link(old_node, links))
    return new_nodes

def process_split_nodes_image(old_node, images):     
    split_nodes = [] 
    text = old_node.text
    for image in images: 
        sections = text.split(f"![{image[0]}]({image[1]})", 1)
        if len(sections) != 2:
            raise ValueError("Inavlid markdown, image section not closed") 
        if sections[0] != "":
            split_nodes.append(TextNode(sections[0], text_type_text))
        split_nodes.append(TextNode(image[0], text_type_image, image[1]))
        text = sections[1]
    if text.strip():
        split_nodes.append(TextNode(text, text_type_text))
    return split_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
           new_nodes.append(old_node)
           continue
        images = extract_md_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue   
        new_nodes.extend(process_split_nodes_image(old_node, images))
    return new_nodes 

def extract_md_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_md_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches