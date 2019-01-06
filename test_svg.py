from svg import Document

def test_generate_xml():
    doc = Document()
    with doc.tag("svg", 'height="400" width="800"'):
        doc.tag("rect", 'y="20"')
        doc.tag("rect", 'y="30"')
        with doc.tag("g", 'x="20"'):
            with doc.tag("text"):
                doc.text("Hello")
        doc.tag("rect", 'y="40"')

    print(doc.out)

    assert doc.out == '''<svg height="400" width="800" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect y="20"/>
  <rect y="30"/>
  <g x="20">
    <text>
      Hello
    </text>
  </g>
  <rect y="40"/>
</svg>
'''
