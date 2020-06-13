import os
__path__=[os.path.dirname(os.path.abspath(__file__))]

from . import AbstractGraph as ag

# class DGraphModel(ag.AbstractGraph):
#   def __init__(self, nodeList=[]):
#     super().__init__(nodeList=nodeList)

graph = ag.AbstractGraph()

graph.add('0');
graph.add('1');
graph.add('2');
graph.add('3');
graph.add('4');
graph.connect('0', '1', 5);
graph.connect('0', '2', 3);
graph.connect('0', '4', 2);
graph.connect('1', '2', 2);
graph.connect('1', '3', 6);
graph.connect('2', '1', 1);
graph.connect('2', '3', 2);
graph.connect('4', '1', 6);
graph.connect('4', '2', 10);
graph.connect('4', '3', 4);

graph.printGraph()

graph.remove('1');

graph.printGraph()