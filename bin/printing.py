from pprint import pprint

from connect import getConnection
from datalogQuery import datalogQuery
from translator import getTranslation

_all_ = ["pprint","pformat"]

def pprint(object, stream=None, indent=1, width=80, depth=None):
  """------------"""
  printer = PrettyPrinter(
    stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(object)
    
def pformat(object, indent=1, width=80, depth=None);
  """------------"""
  return PrettyPrinter (indent=indent, width=width, depth=depth), pformat(object)



