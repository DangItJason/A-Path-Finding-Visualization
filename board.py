# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:20:56 2020

@author: nguye
"""

class Board:
    def __init__(self):
        self.obstacles = []

    '''
        Returns list of accessible neighbor nodes.
    '''
    def getNeighbors(self, Neighbor):
        from node import Node
        ret = []
        i = Neighbor.x
        j = Neighbor.y
        
        '''
        TODO: Check for obstacles
        '''
        if i - 1 >= 0 and j >= 0 and (i - 1, j) not in self.obstacles:
            ret.append(Node(i - 1, j, 0, 0))
        if i >= 0 and j - 1 >= 0 and (i, j - 1) not in self.obstacles:
            ret.append(Node(i, j - 1, 0, 0))
        if i - 1 >= 0 and j - 1 >= 0 and (i - 1, j - 1) not in self.obstacles:
            ret.append(Node(i - 1, j - 1, 0, 0))
        if i + 1 < 100 and j >= 0 and (i + 1, j) not in self.obstacles:
            ret.append(Node(i + 1, j, 0, 0))
        if i >= 0 and j + 1 < 100 and (i, j + 1) not in self.obstacles:
            ret.append(Node(i, j + 1, 0, 0))
        if i + 1 < 100 and j - 1 >= 0 and (i + 1, j - 1) not in self.obstacles:
            ret.append(Node(i + 1, j - 1, 0, 0))
        if i - 1 >= 0 and j + 1 < 100 and (i - 1, j + 1) not in self.obstacles:
            ret.append(Node(i - 1, j + 1, 0, 0))
        if i + 1 < 100 and j + 1 < 100 and (i + 1, j + 1) not in self.obstacles:
            ret.append(Node(i + 1, j + 1, 0, 0))

        return ret
    
    
    '''
        Adds (x, y) coordinate pair to obstacles list
    '''
    def addObstacle(self, coord):
        if (coord not in self.obstacles):
            self.obstacles.append(coord)