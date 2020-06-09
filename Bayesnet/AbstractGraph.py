class VertexNode():
  def __init__(self, value, inList=[], outList=[], totalIn=0, totalOut=0):
    self.value = value
    self.inList = inList
    self.outList = outList
    self.totalIn = totalIn
    self.totalOut = totalOut

class Edge():
  def __init__(self, fromNode, toNode):
    self.fromNode = fromNode
    self.toNode = toNode

class AbstractGraph():
  def __init__(self):
    super().__init__()