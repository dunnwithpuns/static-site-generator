import os
import shutil
from pathlib import Path

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
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    
    template = template.replace("""{{ Title }}""", title)
    template = template.replace("""{{ Content }}""", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    with open(dest_path, mode="a") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path , dest_path)
        else:
            generate_pages_recursive((from_path), template_path, dest_path)
