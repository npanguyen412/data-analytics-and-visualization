import os
__path__=[os.path.dirname(os.path.abspath(__file__))]

from . import AbstractGraph as ag

# class DGraphModel(ag.AbstractGraph):
#   def __init__(self, nodeList=[]):
#     super().__init__(nodeList=nodeList)

graph = ag.AbstractGraph()
for idx in range(10):
  graph.add(str(idx))
graph.connect('0', '1')
graph.connect('0', '5')
graph.connect('1', '7')
graph.connect('3', '2')
graph.connect('3', '4')
graph.connect('3', '7')
graph.connect('3', '8')
graph.connect('4', '8')
graph.connect('6', '0')
graph.connect('6', '1')
graph.connect('6', '2')
graph.connect('8', '2')
graph.connect('8', '7')
graph.connect('9', '4')

graph.printGraph()