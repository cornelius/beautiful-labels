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
        self.text('<?xml version="1.0" standalone="no"?>')
        self.text('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')

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

def calculate_lines(labels):
    lines = []
    for category in labels.all_categories():
        line_labels = []
        for label in labels.labels_for_category(category):
            line_labels.append(label)
        lines.append((category, line_labels))
    return lines

def write_text(doc, text, size=20, fill="black", x="0", y="0"):
    with doc.tag('g', 'font-size="%s" font-family="arial" fill="%s"' % (size, fill)):
        with doc.tag('text', 'x="%s" y="%s"' % (x, y)):
            doc.text(text)

def write_rect(doc, x=0, y=0, width=10, height=10, fill="black"):
    doc.tag('rect', 'x="%s" y="%s" width="%s" height="%s" fill="%s" rx="5"' % (x, y, width, height, fill))

def write_svg(labels, filename):
    doc = Document()
    with doc.tag('svg', 'width="600" height="400"'):
        doc.tag('rect', 'x="0" y="0" width="600" height="220" fill="#eee"')

        write_text(doc, "Labels for %s/%s" % (labels.org, labels.repo), size=30, fill="#444", x=40, y=50)

        lines = calculate_lines(labels)
        line_y = 120
        for category, labels_line in lines:
            write_text(doc, category, size=30, fill="#777", x=40, y=line_y)

            label_x = 250
            for label in labels_line:
                write_rect(doc, x=label_x, y=line_y-30, width=120, height=40, fill="#" + label["color"])
                write_text(doc, label["name"], fill="white", x=label_x+13, y=line_y-4)

                label_x += 140

            line_y += 60

    with open(filename, "w") as file:
        file.write(doc.out)
