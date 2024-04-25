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
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props_to_html()})")