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
        self.text("<!--\n    This file was generated by `beautiful-labels`. Don't edit it directly.\n-->")

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
        line_header = category
        line_labels = []
        for label in labels.labels_for_category(category):
            line_labels.append(label)
            if len(line_labels) == 4:
                lines.append((line_header, line_labels.copy()))
                line_labels.clear()
                line_header = ""
        if line_labels:
            lines.append((line_header, line_labels))
    return lines

def text_color(background_color):
    (r,g,b) = tuple(int(background_color[i:i+2], 16) for i in (0, 2 ,4))
    # See https://www.w3.org/TR/AERT/#color-contrast for details about the formula
    brightness = (0.299*r + 0.587*g + 0.114*b)
    if brightness > 186:
        return "black"
    else:
        return "white"

def write_text(doc, text, size=20, fill="black", x="0", y="0"):
    with doc.tag('g', 'font-size="%s" font-family="arial" fill="%s"' % (size, fill)):
        with doc.tag('text', 'x="%s" y="%s"' % (x, y)):
            doc.text(text)

def write_rect(doc, x=0, y=0, width=10, height=10, fill="black"):
    doc.tag('rect', 'x="%s" y="%s" width="%s" height="%s" fill="%s" rx="5"' % (x, y, width, height, fill))

def write_svg(labels, filename, label_font_size=14):
    lines = calculate_lines(labels)

    line_height = 60

    image_width = 840
    image_height = 100 + len(lines) * line_height

    doc = Document()
    with doc.tag('svg', 'width="%s" height="%s"' % (image_width, image_height)):
        doc.tag('rect', 'x="0" y="0" width="%s" height="%s" fill="#eee"' % (image_width, image_height))

        write_text(doc, "Labels for %s/%s" % (labels.org, labels.repo), size=25, fill="#444", x=40, y=50)

        line_y = 120
        for category, labels_line in lines:
            if category:
                write_text(doc, category, size=25, fill="#777", x=40, y=line_y)

            label_x = 200
            for label in labels_line:
                write_rect(doc, x=label_x, y=line_y-30, width=130, height=40, fill="#" + str(label["color"]))
                write_text(doc, label["name"], size=label_font_size, fill=text_color(str(label["color"])), x=label_x+13, y=line_y-4)

                label_x += 150

            line_y += line_height

    with open(str(filename), "w") as file:
        file.write(doc.out)
