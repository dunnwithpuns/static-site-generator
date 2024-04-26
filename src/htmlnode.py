class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""

        for key, value in self.props.items():
            output += f''' {key}=\"{value}\"'''

        return output

    def __repr__(self):
        children_repr = 'None' if self.children is None else self.children
        props_repr = 'None' if self.props is None else self.props_to_html() 
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children={children_repr}, props={props_repr})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):

        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        elif self.tag == None:
            return self.value
        else:
            props_str = self.props_to_html() if self.props else ""
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}"
        