class Edge():
  def __init__(self, fromNode, toNode, weight=0):
    self.fromNode = fromNode
    self.toNode = toNode
    self.weight = float(weight)

  # Adjust the weight of an Edge
  def weight(self, weight):
    self.weight = float(weight)