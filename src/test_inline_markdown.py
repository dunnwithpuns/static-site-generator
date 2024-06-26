import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_md_images,
    extract_md_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class testInlineMarkdown(unittest.TestCase):
    def test_split_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text),]
        self.assertEqual(new_nodes, expected)

    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected =[
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_delimiter_error(self):
        node = TextNode("This is an incorrecly **bolded word", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", text_type_bold)

    def test_extract_md_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(extract_md_images(text), expected)

    def test_extract_md_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_md_links(text), expected)

    def test_split_nodes_image_single(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) cool!", text_type_text)
        expected = [
            TextNode("This is text with an ", text_type_text), 
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
            TextNode(" cool!", text_type_text), 
            ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_spilt_nodes_image_double(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text)
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            ] 
        self.assertEqual(split_nodes_image([node]), expected)
    
    # def test_split_nodes_image_err(self):
    #     node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png cool!", text_type_text)
    #     with self.assertRaises(ValueError):
    #         split_nodes_image([node])

    def test_split_nodes_link_single(self):
        node = TextNode("This is text with a [link](https://www.google.com) cool!", text_type_text)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.google.com"),
            TextNode(" cool!", text_type_text),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_link_double(self):
        node = TextNode("This is text with a [link](https://www.google.com) and another [second link](https://www.boot.dev)", text_type_text)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.google.com"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://www.boot.dev"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)
    
    # def test_split_nodes_link_err(self):
    #     node = TextNode("This is text with a [link](https://www.google.com", text_type_text)
    #     with self.assertRaises(ValueError):
    #         split_nodes_link([node])

    def test_split_nodes_link_multiple(self):
        node1 = TextNode("This is text with a [link](https://www.google.com) cool!", text_type_text)
        node2 = TextNode("This is text with a [link](https://www.google.com) and another [second link](https://www.boot.dev) cool!", text_type_text)
        node_list = [node1, node2]
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.google.com"),
            TextNode(" cool!", text_type_text),
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.google.com"), 
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://www.boot.dev") 
        ]
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
     unittest.main()