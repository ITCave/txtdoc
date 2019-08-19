# -*- coding: utf-8 -*-
# @Filename : document
# @Date : 2019-08-14-11-24
# @Poject: ITC-txtdoc
# @Author: Piotr Wołoszyn
# @Website: http://itcave.eu
# @Email: contact@itcave.eu
# @License: MIT
# @Copyright (C) 2019 ITGO Piotr Wołoszyn

from txtdoc.abstract import TxtContainer
from txtdoc.paragraph import TxtParagraph
import os


class TxtDoc(TxtContainer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_run(self, text, align='left') -> TxtParagraph:
        """
        Method that adds text run to the document
        :param text: str
        :param align: one of ('left', 'right', 'center')
        :return: text paragraph (TxtParagraph)
        """
        p = TxtParagraph(self, align=align)
        p.append(text)
        self.append(p)
        return p

    def hr(self, text='', align='center', c='-'):
        """
        Helper/Shortcut that draws a horizontal line (with optional text)
        :return: TxtParagraph
        """

        p = TxtParagraph(self, align=align)

        if len(text) > self.inner_width:
            text = text[:self.inner_width]

        if align == 'center':
            line_format = '{0:' + c + '^{width}}'
        elif align == 'left':
            line_format = '{0:' + c + '<{width}}'
        elif align == 'right':
            line_format = '{0:' + c + '>{width}}'
        else:
            raise AttributeError('Not allowed align value, it should be of of: center, left, right')

        text = line_format.format(text, width=self.inner_width)

        p.append(text)
        self.append(p)

        return p

    def br(self):
        """
        Helper/Shortcut method prints the line break
        :return: TxtParagraph
        """

        p = self.add_run("\n")
        return p

    def page_break(self):
        """
        Puts pagebreak in the file
        :return:
        """
        p = self.add_run("\f")
        return p

    def save(self, path, encoding='UTF-8'):
        """
        Saves buffer to file
        :param path:
        :param encoding:
        :return:
        """

        if os.path.exists(os.path.dirname(path)):
            with open(path, 'w', encoding=encoding) as f:
                content = self.render()
                f.write(content)
        else:
            raise FileExistsError("Path <" + str(path.dirname(path)) + "> does not exist")


if __name__ == '__main__':
    pass
