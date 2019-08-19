# -*- coding: UTF-8 -*-

from txtdoc.document import TxtDoc
from txtdoc.layout import ColumnLayout, TxtColumn

if __name__ == '__main__':

    doc = TxtDoc(width=100, margins=(2, 2), eol="\n")

    c_layout = ColumnLayout(doc)
    doc.append(c_layout)

    pierwsza = c_layout.add_column('pierwsza', 50)
    pierwsza.add_run("Test")

    title = doc.add_run("THIS IS A VERY NICE PAGE TITLE", align="center")
    title.border.width = 1
    title.border.padding = 1
    title.border.style = '@'

    doc.br()
    doc.hr(" LEFT aligned paragraph ")
    doc.br()
    left_p = doc.add_run(
        "Hi!\nI'm a paragraph that demonstrates LEFT text alignment!\n Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Amet luctus venenatis lectus magna fringilla urna porttitor rhoncus dolor.\n Venenatis cras sed felis eget.\n "
        "Tristique et egestas quis ipsum suspendisse ultrices gravida. Elementum tempus egestas sed sed risus "
        "pretium quam vulputate dignissim.\n",
        align='left')

    doc.hr(" RIGHT aligned paragraph ")
    doc.br()
    right_p = doc.add_run(
        "I'm a paragraph that demonstrates RIGHT text alignment!\n Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Amet luctus venenatis lectus magna fringilla urna porttitor rhoncus dolor. Venenatis cras sed felis eget.\n "
        "Tristique et egestas quis ipsum suspendisse ultrices gravida. Elementum tempus egestas sed sed risus "
        "pretium quam vulputate dignissim.\n",
        align='right')

    doc.hr(" CENTERED paragraph ")
    doc.br()
    center_p = doc.add_run(
        "I'm a paragraph that demonstrates CENTER text alignment!\n Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Amet luctus venenatis lectus magna fringilla urna porttitor rhoncus dolor. Venenatis cras sed felis eget.\n "
        "Tristique et egestas quis ipsum suspendisse ultrices gravida. Elementum tempus egestas sed sed risus "
        "pretium quam vulputate dignissim.",
        align='center')

    center_p.append("\n\nAnd this is how you can append text to the existing paragraph\n\n")

    hr = doc.hr(" I'm a horizontal line with example text ")  # Horizontal line with text
    doc.br()
    hr2 = doc.hr(" And i'm made of stars ", c="*")  # Horizontal line with text
    doc.br()

    print(doc.render())

