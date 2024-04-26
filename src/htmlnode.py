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

        for i in self.props:
            output += f"{i}={self.props[i]} "

        output = output.rstrip(" ")
        return output

    def __repr__(self):
        children_repr = 'None' if self.children is None else self.children
        props_repr = 'None' if self.props is None else self.props_to_html() 
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children={children_repr}, props={props_repr})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__()
    
    def to_html(self):

        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}"