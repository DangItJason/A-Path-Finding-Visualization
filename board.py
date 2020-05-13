# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:20:56 2020

@author: nguye
"""

class Board:
    def __init__(self):
        self.board = []
#        for i in range(0, 100):
#            for j in range(0, 100):
#               ##Fill w/ desired obstacles
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
        if i - 1 >= 0 and j >= 0:
            ret.append(Node(i - 1, j, 0, 0))
        if i >= 0 and j - 1 >= 0:
            ret.append(Node(i, j - 1, 0, 0))
        if i - 1 >= 0 and j - 1 >= 0:
            ret.append(Node(i - 1, j - 1, 0, 0))
        if i + 1 < 100 and j >= 0:
            ret.append(Node(i + 1, j, 0, 0))
        if i >= 0 and j + 1 < 100:
            ret.append(Node(i, j + 1, 0, 0))
        if i + 1 < 100 and j - 1 >= 0:
            ret.append(Node(i + 1, j - 1, 0, 0))
        if i - 1 >= 0 and j + 1 < 100:
            ret.append(Node(i - 1, j + 1, 0, 0))
        if i + 1 < 100 and j + 1 < 100:
            ret.append(Node(i + 1, j + 1, 0, 0))

        return ret  