from svg import Document

def test_generate_xml():
    doc = Document()
    with doc.tag("svg", width="800", height="400"):
        with doc.tag("g", x="20"):
            with doc.tag("text"):
                doc.text("Hello")
        doc.tag("rect", y="40")

    print(doc.out)

    assert doc.out == '''<svg height='400' width='800'>
  <g x='20'>
    <text>
      Hello
    </text>
  </g>
  <rect y='40'>
</svg>
'''
