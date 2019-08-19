# -*- coding: UTF-8 -*-

from txtdoc.document import TxtDoc
from txtdoc.layout import ColumnLayout, TxtColumn

if __name__ == '__main__':

    doc = TxtDoc(width=100, margins=(2, 2), eol="\n")

    title = doc.add_run("EXAMPLE TITLE DECORED WITH CUSTOM BORDER MADE OF STARS (OF SORT)", align="center")
    title.set_border(1, 1, style="*")

    doc.br()

    intro = doc.add_run("This is an example document created with txtdoc. While the library is most certainly far from "
                        "perfect it does a decent job at creating basic text documents. It contains a basic suite of "
                        "tools that allow creating relatively complex plain text structures. Possile use cases are "
                        "listed below:\n")

    use_list = doc.add_run("XTODO Placeholder for list")

    doc.br()
    doc.hr()
    doc.hr(" \"Line\" with text example ")
    doc.br()
    doc.hr("LEFT ALIGNED ", align='left', c='<')

    doc.add_run("This is an example of LEFT aligned text block: Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit. Etiam ac faucibus odio. Pellentesque felis tortor, commodo nec lacinia vehicula, ornare at "
                "sapien. Mauris vel orci ac nisi aliquam aliquet sit amet eget lectus. ", align='left')
    doc.br()
    doc.hr(" RIGHT ALIGNED", align='right', c='>')

    doc.add_run("This is an example of RIGHT aligned text block: Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit. Etiam ac faucibus odio. Pellentesque felis tortor, commodo nec lacinia vehicula, ornare at "
                "sapien. Mauris vel orci ac nisi aliquam aliquet sit amet eget lectus. ", align='right')

    doc.br()
    doc.hr(" CENTERED ", align='center', c='^')

    doc.add_run("This is an example of CENTERED text block: Lorem ipsum dolor sit amet, consectetur adipiscing "
                "elit. Etiam ac faucibus odio. Pellentesque felis tortor, commodo nec lacinia vehicula, ornare at "
                "sapien. Mauris vel orci ac nisi aliquam aliquet sit amet eget lectus. ", align='center')

    doc.br()
    doc.br()
    doc.add_run(" COLUMN LAYOUT EXAMPLE ", align='center')

    c_layout = ColumnLayout(doc)
    doc.append(c_layout)

    first_column = c_layout.add_column('first', 31, (1, 0))
    second_column = c_layout.add_column('second', 31, (1, 0))
    third_column = c_layout.add_column('third', 31, (1, 0))

    first_title = first_column.add_run("ENGLISH", align='center')
    first_title.set_border(width=0, padding=1)
    first_column.add_run("This is an example that shows how to build simple column layout using txtdoc library!")

    second_title = second_column.add_run("DEUTSCH", align='center')
    second_title.set_border(width=0, padding=1)
    second_column.add_run("Dies ist ein Beispiel, das zeigt, wie ein einfaches Spaltenlayout mit der txtdoc-Bibliothek "
                          "erstellt werden kann!")

    third_title = third_column.add_run("POLSKI", align='center')
    third_title.set_border(width=0, padding=1)
    third_column.add_run("To przykład, który pokazuje, jak zbudować prosty układ kolumn za pomocą biblioteki txtdoc!")

    print(doc.render())

