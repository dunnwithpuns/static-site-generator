class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_html = ""
        if self.props is None:
            return props_html

        for key, value in self.props.items():
            props_html += f''' {key}="{value}"'''

        return props_html.rstrip()

    def __repr__(self): 
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children},{self.props_to_html()})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        elif self.tag == None:
            return self.value

        props_str = self.props_to_html() if self.props else ""

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props) 
        
    def to_html(self):

        if not self.children:
            raise ValueError("A parent node requires a child!")
        if not self.tag:
            raise ValueError("Please provide a tag")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"