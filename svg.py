class Tag:
    def __init__(self, doc, name):
        self.doc = doc
        self.name = name

    def __enter__(self):
        self.doc.level += 1

    def __exit__(self, type, value, traceback):
        self.doc.level -= 1
        if self.doc.open_tag:
            self.doc.out += "/>\n"
            self.open_tag = False
        self.doc.indent()
        self.doc.out += "</" + self.name + ">\n"

class Document:
    def __init__(self):
        self.level = 0
        self.last_level = 0
        self.out = ""
        self.open_tag = False

    def indent(self):
        self.out += self.level * '  '

    def tag(self, name, attributes=None):
        if self.open_tag:
            if self.last_level == self.level:
                self.out += "/>\n"
            else:
                self.out += ">\n"
            self.open_tag = False
        self.indent()
        self.out += "<" + name
        if attributes:
            self.out += ' ' + attributes
        if name == "svg":
            self.out += ' xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'
        self.open_tag = True
        self.last_level = self.level
        return Tag(self, name)

    def text(self, text):
        if self.open_tag:
            self.out += ">\n"
            self.open_tag = False
        self.indent()
        self.out += text + "\n"

def write_svg(labels, filename):
    doc = Document()

    doc.text('<?xml version="1.0" standalone="no"?>')
    doc.text('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')
    with doc.tag('svg', 'width="600" height="400"'):
        doc.tag('rect', 'x="0" y="0" width="600" height="220" fill="#eee"')

        with doc.tag('g', 'font-size="30" font-family="arial" fill="#444"'):
            with doc.tag('text', 'x="40" y="50"'):
                doc.text("Labels for someorg/somerepo")

        with doc.tag('g', 'font-size="30" font-family="arial" fill="#777"'):
            with doc.tag('text', 'x="40" y="120"'):
                doc.text("Type")

        doc.tag('rect', 'x="250" y="90" width="120" height="40" fill="#d73a4a" rx="5"')
        with doc.tag('g', 'font-size="20" font-family="arial" fill="white"'):
            with doc.tag('text', 'x="263" y="116"'):
                doc.text("bug")

        with doc.tag('g', 'font-size="30" font-family="arial" fill="#777"'):
            with doc.tag('text', 'x="40" y="180"'):
                doc.text("Components")

        doc.tag('rect', 'x="250" y="150" width="120" height="40" fill="#EE7912" rx="5"')
        with doc.tag('g', 'font-size="20" font-family="arial" fill="white"'):
            with doc.tag('text', 'x="263" y="176"'):
                doc.text("frontend")
        doc.tag('rect', 'x="390" y="150" width="120" height="40" fill="#123456" rx="5"')
        with doc.tag('g', 'font-size="20" font-family="arial" fill="white"'):
            with doc.tag('text', 'x="403" y="176"'):
                doc.text("backend")

    with open(filename, "w") as file:
        file.write(doc.out)
