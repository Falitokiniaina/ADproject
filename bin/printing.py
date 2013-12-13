from pprint import pprint

import globvar

_all_ = ["pprint","pformat"]

def pprint(object, stream=None, indent=1, width=80, depth=None):
  """------------"""
  printer = PrettyPrinter(
    stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(object)
    
def pformat(object, indent=1, width=80, depth=None);
  """------------"""
  return PrettyPrinter (indent=indent, width=width, depth=depth), pformat(object)



