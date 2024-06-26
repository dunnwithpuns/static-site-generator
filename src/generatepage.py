import os
import shutil

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line
    raise Exception("All pages need a single h1 header.")

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    title = extract_title(markdown)
    html = markdown_to_html_node(markdown)
    html = html.to_html()
    
    template.replace("""{{ Title }}""", title)
    template.replace("""{{ Content }}""", html)

    with open(dest_path, mode="a") as f:
        f.write(template)