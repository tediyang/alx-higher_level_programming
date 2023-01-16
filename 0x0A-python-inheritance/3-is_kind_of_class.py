#!/usr/bin/python3
'''kind_of_class module'''


def is_kind_of_class(obj, a_class):
  '''Check if obj is a subclass of a_class'''
  return issubclass(obj, a_class)
