# -*- coding: utf-8 -*-

from splendor.models.boards import TableBoard


table = TableBoard()
print(table.as_dict())
print()

table.setup(4)
print(table.as_dict())
print()

table.setup(3)
print(table.as_dict())
print()
