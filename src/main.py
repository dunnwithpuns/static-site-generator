from textnode import TextNode

from htmlnode import HTMLNode, LeafNode

def main():
    print(TextNode("This is a text node", "bold", "https://www.boot.dev"))
    node = LeafNode("p", "This is a paragraph of text.", {"href": "https://www.google.com"}) 
    print(node.to_html())


if __name__ == "__main__":
    main()