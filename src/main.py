import os
import shutil

from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive, generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print(f"Deleting public directory. . .")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print(f"Copying files to public directory. . .")
    copy_files_recursive(dir_path_static, dir_path_public)
 
    generate_pages_recursive(dir_path_content, template_path, dir_path_public) 

if __name__ == "__main__":
    main()