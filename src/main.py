from textnode import TextNode

from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print(TextNode("This is an image link", "image", "https://www.google.com"))


if __name__ == "__main__":
    main()