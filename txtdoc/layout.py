# -*- coding: utf-8 -*-
# @Filename : layout.py
# @Date : 2019-08-14-16-22
# @Poject: ITC-txtdoc
# @Author: Piotr Wołoszyn
# @Website: http://itcave.eu
# @Email: contact@itcave.eu
# @License: MIT
# @Copyright (C) 2019 ITGO Piotr Wołoszyn

from pprint import pprint

from txtdoc.abstract import TxtObject, TxtContainer
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
        super(AbstractLayout, self).__init__(*args, **kwargs)
        super(OrderedDict, self).__init__()

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
            super(OrderedDict, self).__setitem__(key, value)

    def add_column(self, key, width, margins=(0,)):
        # Placeholder XTODO Shortcut function
        c = TxtColumn(parent=None, width=width, margins=margins)
        self[key] = c
        return self[key]

    def total_column_width(self):

        total_width = 0

        for k, v in self.items():
            total_width += v.width + v.mr + v.ml

        return total_width

    def render(self):

        content = OrderedDict
        self.max_rows = 0

        for k, v in self.items():
            content[k] = v.render().split('\n')

            if len(content[k]) > self.max_rows:
                self.max_rows = len(content[k])

        for k in self.items():
            print(k)


if __name__ == '__main__':
    cl = ColumnLayout(None)
    cl['first_column'] = TxtColumn(width=30, margins=(1, 1))

    pprint(cl)

    pass
