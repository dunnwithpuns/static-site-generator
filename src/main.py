import os
import shutil

from copystatic import copy_files
from generatepage import generate_pages_recursive, generate_page

dir_path_static = "./static"
dir_path_public = "./public"
template_path = "./template.html"
html_path = "./public/index.html"
markdown_path = "./content/majesty/index.html"

def main():
    print(f"Deleting public directory. . .")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print(f"Copying files to public directory. . .")
    copy_files(dir_path_static, dir_path_public)
 
    generate_page(markdown_path, template_path, html_path) 

if __name__ == "__main__":
    main()