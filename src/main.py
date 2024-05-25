from textnode import TextNode

from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print(TextNode("This is an image link", "image", "https://www.google.com"))

    test_var = "a"
    test_int = "1"
    print(type(int(test_var)))
    print(type(int(test_int)))

if __name__ == "__main__":
    main()