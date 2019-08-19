# -*- coding: utf-8 -*-
# @Filename : paragraph
# @Date : 2019-08-14-11-28
# @Poject: ITC-txtdoc
# @Author: Piotr Wołoszyn
# @Website: http://itcave.eu
# @Email: contact@itcave.eu
# @License: MIT
# @Copyright (C) 2019 ITGO Piotr Wołoszyn

from txtdoc.abstract import TxtObject, TxtContainer
from pprint import pprint

class TxtBorder(object):

    def __init__(self, parent, width=0, padding=0, style='*'):
        self.parent = parent
        self.width = width
        self.padding = padding
        self.style = style

    def draw_top(self):

        content = ''

        ml = self.parent.ml
        mr = self.parent.mr
        eol = self.parent.eol

        for i in range(0, self.width):
            line = (" " * ml) + (self.style * self.parent.width) + (" " * mr) + eol
            content += line

        for i in range(0, self.padding):
            line = (" " * ml) + (self.style * self.width) + ((self.parent.width - (2*self.width)) * ' ') \
                   + (self.style * self.width) + (" " * mr) + eol
            content += line

        return content

    def draw_bottom(self):

        content = ''

        ml = self.parent.ml
        mr = self.parent.mr
        eol = self.parent.eol

        for i in range(0, self.padding):
            line = (" " * ml) + (self.style * self.width) + ((self.parent.width - (2*self.width)) * ' ') \
                   + (self.style * self.width) + (" " * mr) + eol
            content += line

        for i in range(0, self.width):
            line = (" " * ml) + (self.style * self.parent.width) + (" " * mr) + eol
            content += line

        return content

    def wrap(self, txt):
        line = (self.style * self.width) + (self.padding * ' ') + txt + (self.padding * ' ') + (self.style * self.width)
        return line


class TxtParagraph(TxtObject):
    def __init__(self, parent: TxtContainer, align='left'):
        self.parent = parent
        self.align = align
        self.border = TxtBorder(self, 0, 0)
        self.text_buffer = []

    @property
    def ml(self):
        return self.parent.ml

    @property
    def mr(self):
        return self.parent.mr

    @property
    def eol(self):
        return self.parent.eol

    @property
    def width(self):
        return self.parent.inner_width

    @property
    def inner_width(self):
        return self.width - (self.border.width*2) - (self.border.padding*2)

    def set_border(self, width=0, padding=0, style='*') -> TxtBorder:
        """
        Helper function to set a border
        :param width:
        :param padding:
        :param style:
        :return:
        """
        self.border = TxtBorder(self, width, padding, style)

    def append(self, text):
        """
        Appends string to the current paragraph
        :param text: text
        """

        t_list = text.split('\n')
        t_count = len(t_list)
        i = 0

        for t in t_list:

            i += 1

            if i != t_count:
                t += '\n'

            words = t.split(' ')
            self.text_buffer += words

    def writeln(self, txt):
        """
        Prepares a line
        :param txt: str
        :return:
        """

        if type(txt) is list:

            content = ''

            for t in txt:
                content += self.writeln(t)

            return content
        else:
            if self.align == 'center':
                line_format = '{0: ^{width}}'
            elif self.align == 'left':
                line_format = '{0: <{width}}'
            elif self.align == 'right':
                line_format = '{0: >{width}}'
            else:
                raise AttributeError('Not allowed align value, it should be of of: center, left, right')

            inner_line = self.border.wrap(line_format.format(txt, width=self.inner_width))

            line = self.parent.wrap_line(inner_line)

            return line

    def render(self):

        content = ''
        line = ''

        if self.border:
            content += self.border.draw_top()

        for word in self.text_buffer:

            ltmp = (line + ' ' + word).lstrip().rstrip('\n')

            if len(ltmp) > self.width:
                content += self.writeln(line)
                line = word
            else:
                line = ltmp
                if len(word) > 0 and word[-1] == '\n':
                    content += self.writeln(line)
                    line = ''

        if len(line) > 0:
            content += self.writeln(line)

        content += self.border.draw_bottom()

        return content


if __name__ == '__main__':
    pass
