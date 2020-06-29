import numpy as np
import pandas as pd
from graph.Edge import Edge

class VertexNode():
  def __init__(self, value):
    self.value = value
    self.inNodes = []
    self.outNodes = []
    self.totalIn = 0
    self.totalOut = 0
    self.inwardEdges = []
    self.outwardEdges = []
    self.probDist = []

  # Connect to another VertexNode
  def connect(self, toNode, weight=0):
    if toNode not in self.outNodes:
      self.outNodes.append(toNode)
      self.totalOut += 1
      toNode.inNodes.append(self)
      toNode.totalIn += 1
      edge = Edge(self, toNode, weight)
      self.outwardEdges.append(edge)
      toNode.inwardEdges.append(edge)
    # else:
    #   raise Exception('Already connected!')

  # Print inNodes, outNodes, inwardEdges or outwardEdges of a node
  def printInOut(self, type='Node', dir='In'):
    print('+'*20)
    data = []
    lst = []
    DF = []
    if type == 'Node':
      if dir == 'In':
        lst = self.inNodes
      elif dir == 'Out':
        lst = self.outNodes
      for node in lst:
        data.append(node.value)
      print(dir + 'Nodes of {}'.format(self.value))
      DF = pd.DataFrame(np.array(data), columns=['Node'])
    elif type == 'Edge':
      if dir == 'In':
        lst = self.inwardEdges
      elif dir == 'Out':
        lst = self.outwardEdges
      for edge in lst:
        data.append([edge.fromNode.value, edge.toNode.value, edge.weight])
      print(dir + 'wardEdges of {}'.format(self.value))
      DF = pd.DataFrame(np.array(data), columns=['From', 'To', 'Weight'])
    print(DF)
    print('+'*20)

  # Disconnect a connected VertexNode from another VertexNode
  @staticmethod
  def disconnect(fromNode, toNode):
    if (toNode in fromNode.outNodes) & (fromNode in toNode.inNodes):
      edge = (VertexNode).getEdge(fromNode, toNode)
      if edge is not None:
        fromNode.outNodes.remove(toNode)
        fromNode.totalOut -= 1
        toNode.inNodes.remove(fromNode)
        toNode.totalIn -= 1
        fromNode.outwardEdges.remove(edge)
        toNode.inwardEdges.remove(edge)
      # else:
      #   raise Exception('Edge not found!')
    # else:
    #   raise Exception('Not connected!')

  # Get edge between VertexNodes
  @staticmethod
  def getEdge(fromNode, toNode):
    if (toNode in fromNode.outNodes) & (fromNode in toNode.inNodes):
      for edge in fromNode.outwardEdges:
        if (edge.fromNode is fromNode) & (edge.toNode is toNode):
          return edge
        else:
          return None
    else:
      return None