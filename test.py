# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:52:54 2020

@author: nguye
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:19:16 2020

@author: nguye
"""

class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        
    def __eq__(self, obj):
        if not isinstance(obj, Node):
            return NotImplemented
        
        return self.x == obj.x and self.y == obj.y
    
    def __lt__(self, obj):
        if not isinstance(obj, Node):
            return NotImplemented
        
        return (self.g + self.h) < (obj.g + obj.h)
    
    '''
        Returns Euclidean distance between neighbor and current node.
    '''
    def getGScore(self, neighbor):
        return ((self.x - neighbor.x)**2 + (self.y - neighbor.y)**2)**1/2
    
    
    '''
        Returns the Manhattan distance between current and end node
    '''
    def getHScore(self, end):
        return abs(self.x - end.x) + abs(self.y - end.y)

print(Node(0, 0 ,0 ,0) == Node(0,1,0,0))