# -*- coding: utf-8 -*-
# @Filename : layout.py
# @Poject: txtdoc
# @Author: Piotr Wołoszyn
# @Website: http://itcave.eu
# @Email: contact@itcave.eu
# @License: MIT
# @Copyright (C) 2019 ITGO Piotr Wołoszyn

from pprint import pprint

from txtdoc.base import TxtObject, TxtContainer
from txtdoc.document import TxtDoc

from collections import OrderedDict


class AbstractLayout(TxtObject):

    def __init__(self):
        pass

    def render(self):
        pass


class TxtColumn(TxtDoc):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, path, encoding='UTF-8'):
        pass


class ColumnLayout(AbstractLayout, OrderedDict):

    def __init__(self, parent: TxtContainer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.width = parent.inner_width
        self.max_rows = 0

    def __setitem__(self, key, value):
        if not issubclass(type(value), TxtColumn):
            raise TypeError("Set attribute must be a subclass of TxtColumn")
        else:
            total_width = self.total_column_width() + value.width
            if total_width > self.width:
                raise ValueError("Total sum of column widths exceeds the maximum allowed width (%s > %s) "
                                 % (total_width, self.width))
            super().__setitem__(key, value)

    def add_column(self, key, width, margins=(0,)) -> TxtColumn:
        # Placeholder XTODO Shortcut function
        c = TxtColumn(parent=None, width=width, margins=margins)
        self.__setitem__(key, c)
        return self[key]

    def total_column_width(self):

        total_width = 0

        for k, v in self.items():
            total_width += v.width + v.mr + v.ml

        return total_width

    def render(self):

        c_content = OrderedDict()
        self.max_rows = 0

        for k, col in self.items():

            c_content[k] = col.render().split('\n')

            if len(c_content[k]) > 1:
                c_content[k] = c_content[k][:-1]

            if len(c_content[k]) > self.max_rows:
                self.max_rows = len(c_content[k])

        content = ''

        for i in range(0, self.max_rows):

            line = ''

            for k, c in c_content.items():
                try:
                    line += c[i]
                except IndexError:
                    line += ' ' * self[k].width
                except Exception:
                    raise
            line = self.parent.wrap_line(line)
            content += line

        return content


if __name__ == '__main__':

    pass
