# -*- coding: utf-8 -*-
# @Filename : abstract
# @Date : 2019-08-14-11-22
# @Poject: ITC-txtdoc
# @Author: Piotr Wołoszyn
# @Website: http://itcave.eu
# @Email: contact@itcave.eu
# @License: MIT
# @Copyright (C) 2019 ITGO Piotr Wołoszyn

from abc import ABCMeta, abstractmethod


class TxtObject(metaclass=ABCMeta):
    pass

    @abstractmethod
    def render(self):
        pass


class TxtContainer(TxtObject):

    def __init__(self, parent=None, width=80, margins=(0,), eol='\n'):
        super().__init__()

        if not (isinstance(margins, tuple) or isinstance(margins, list)):
            raise AttributeError("Attribute <margin> must be a list or a tuple")

        self.width = width
        self.ml = 0
        self.mr = 0
        self.set_margins(margins)
        self.eol = eol

        self._children = []

    @property
    def inner_width(self):
        return self.width - self.ml - self.mr

    def set_margins(self, margins=(0,)):
        """
        Method that sets both margins
        :param margins: tuple or list
        :return: void
        """
        if len(margins) == 1:
            self.ml = int(margins[0])
            self.mr = int(margins[0])
        elif len(margins) == 2:
            self.ml = int(margins[0])
            self.mr = int(margins[1])
        else:
            raise AttributeError("Attribute <margin> must be of len 1 or 2")

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if issubclass(type(value), list):
            self._children = value
        else:
            raise TypeError("Value set for children of TxtContainer must be a subclass of a list")

    def wrap_line(self, s):
        """
        Method that add margins and eol char to a string
        :param s:
        :return:
        """
        return (" " * self.ml) + s + (" " * self.mr) + self.eol

    def append(self, value):
        """
        Method that appends an item to the container
        :param value:
        :return:
        """
        if issubclass(type(value), TxtObject):
            self._children.append(value)
        else:
            raise TypeError("Appended value must be a subclass of TxtObject")

    def render(self):
        """
        Method that render the document content
        :return: rendered content (str)
        """
        content = ''
        for item in self.children:
            content += item.render()

        return content


if __name__ == '__main__':
    pass
