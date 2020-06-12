import numpy as np
import pandas as pd

class Edge():
  def __init__(self, fromNode, toNode, weight=0):
    self.fromNode = fromNode
    self.toNode = toNode
    self.weight = weight

  # Adjust the weight of an Edge
  def weight(self, weight):
    self.weight = weight

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

  # Disconnect a connected VertexNode from another VertexNode
  @staticmethod
  def disconnect(fromNode, toNode):
    if (toNode in fromNode.outNodes) & (fromNode in toNode.inNodes):
      fromNode.outNodes.remove(toNode)
      fromNode.totalOut -= 1
      toNode.inNodes.remove(fromNode)
      toNode.totalIn -= 1
      edge = getEdge(fromNode, toNode)
      fromNode.outwardEdges.remove(edge)
      toNode.inwardEdges.remove(edge)

  # Get edge between VertexNodes
  @staticmethod
  def getEdge(fromNode, toNode):
    if (toNode in fromNode.outNodes) & (fromNode in toNode.inNodes):
      for edge in fromNode.outwardEdges:
        if (edge.fromNode is fromNode) & (edge.toNode is toNode):
          return edge

class AbstractGraph():
  def __init__(self, nodeList=[]):
    self.nodeList = nodeList

  # Add new VertexNode to the graph
  def add(self, value):
    if self.getVertexNode(value) is None:
      newNode = VertexNode(value)
      self.nodeList.append(newNode)
    # else:
    #   raise Exception('Existed Vertex!')

  # Connect one VertexNode to another
  def connect(self, fromValue, toValue, weight=0):
    fromNode = self.getVertexNode(fromValue)
    toNode = self.getVertexNode(toValue)
    if (fromNode is not None) & (toNode is not None):
      fromNode.connect(toNode, weight)
    # else:
    #   raise Exception('Vertex not found!')

  # Remove a VertexNode from the graph
  def remove(self, value):
    node = self.getVertexNode(value)
    if node is not None:
      for inNode in node.inNodes:
        VertexNode.disconnect(inNode, node)
      for outNode in node.outNodes:
        VertexNode.disconnect(node, outNode)
      self.nodeList.remove(node)
    # else:
    #   raise Exception('Vertex not found!')

  # Get a node from the graph
  def getVertexNode(self, value):
    nodeExist = False
    for node in self.nodeList:
      if node.value == value:
        nodeExist = True
        return node
    if not nodeExist:
      return None

  # Get inward or outward Edges
  def getEdges(self, direction='outward'):
    edges = []
    if direction == 'outward':
      for node in self.nodeList:
        edges.extend(node.outwardEdges)
    elif direction == 'inward':
      for node in self.nodeList:
        edges.extend(node.inwardEdges)
    return edges

  # Print graph info
  def printGraph(self):
    nodes = self.nodeList
    edges = self.getEdges()
    nodeData = []
    edgeData = []
    print('='*40)
    print('Vertices:')
    for node in nodes:
      nodeData.append([node.value, node.totalIn, node.totalOut])
    nodeDF = pd.DataFrame(np.array(nodeData), columns=['Vertex', 'In', 'Out'])
    print(nodeDF)
    print('-'*20)
    print('Edges:')
    for edge in edges:
      edgeData.append([edge.fromNode.value, edge.toNode.value, edge.weight])
    edgeDF = pd.DataFrame(np.array(edgeData), columns=['From', 'To', 'Weight'])
    print(edgeDF)
    print('='*40)
