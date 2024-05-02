from textnode import TextNode

from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = TextNode("This is an image link", "image", "https://www.google.com").text_node_to_html_node()
    expected = LeafNode("img", value="", props={"scr": "https://www.google.com", "alt": "This is an image link"})

    print(node.to_html())
    print(expected.to_html())

if __name__ == "__main__":
    main()