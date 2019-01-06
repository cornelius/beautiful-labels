from svg import Document
from labels import Labels
from svg import calculate_lines

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

    assert doc.out == '''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg height="400" width="800" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
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

def test_calculate_lines():
    labels = Labels("someorg", "somerepo")
    labels.load('test_data/structured-labels.yaml')

    lines = calculate_lines(labels)

    assert lines == [
        ('Type',
            [{'color': 'd73a4a',
              'description': "Something isn't working",
              'id': 1097075204,
              'name': 'bug'}]),
        ('Components',
            [{'color': 'EE7912',
              'description': 'Frontend',
              'id': 1166740325,
              'name': 'frontend'},
             {'color': '123456',
              'description': 'Backend and database',
              'id': 1167038964,
              'name': 'backend'}]),
    ]
