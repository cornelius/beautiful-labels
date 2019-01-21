class Field:
    def __init__(self, query, name):
        self.query = query
        self.name = name

    def __enter__(self):
        self.query.out += " {"
        self.query.level += 1

    def __exit__(self, type, value, traceback):
        self.query.level -= 1
        self.query.out += "\n"
        self.query.indent()
        self.query.out += "}"


class Query():
    def __init__(self):
        self.out = ""
        self.level = 1

    def indent(self):
        self.out += ' ' * 2 * self.level

    def field(self, name, attributes=None):
        self.out += "\n"
        self.indent()
        self.out += name
        if attributes:
            self.out += "(%s)" % attributes
        return Field(self, name)

    def json(self):
        return {"query": "query {%s\n}\n" % self.out}
