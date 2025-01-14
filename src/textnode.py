from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, compare):

        if self.text == compare.text and self.text_type == compare.text_type and self.url == compare.url :
            return True
        else :
            return False
    
    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")