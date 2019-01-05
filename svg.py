class Tag:
    def __init__(self, doc, name):
        self.doc = doc
        self.name = name

    def __enter__(self):
        self.doc.level += 1

    def __exit__(self, type, value, traceback):
        self.doc.level -= 1
        self.doc.indent()
        self.doc.out += "</" + self.name + ">\n"

class Document:
    def __init__(self):
        self.level = 0
        self.out = ""

    def indent(self):
        self.out += self.level * '  '

    def tag(self, name, **attributes):
        self.indent()
        self.out += "<" + name
        for key, value in sorted(attributes.items()):
            self.out += " %s='%s'" % (key, value)
        self.out += ">\n"
        return Tag(self, name)

    def text(self, text):
        self.indent()
        self.out += text + "\n"
