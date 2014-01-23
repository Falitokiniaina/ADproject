class Tree(object):
    def __init__(self, head={}, body={}, type=""):
        self.head = head 
        self.body = body
        self.type = type
    def __repr__(self):
        return "%r" % (self.__dict__)
     
        
class Predicate(object):
    def __init__(self, name="", terms=[], isNegated=""):
        self.name = name
        self.terms = terms
        self.isNegated = isNegated
    def __repr__(self):
        return "%r" % (self.__dict__)
   
   
class Constraint(object):
    def __init__(self, termX="", operator="", termY=""):
        self.termX = termX
        self.operator = operator
        self.termY = termY 
    def __repr__(self):
        return "%r" % (self.__dict__)