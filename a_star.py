# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:08:01 2020

@author: nguye
"""


'''
    Finds path using A* algorithm from https://brilliant.org/wiki/a-star-search/#references
    
    Uses Manhattan distance for calculating heuristic.
    
    Returns path of visited nodes.
'''
def solve(obstacles, app):
    from node import Node
    from board import Board
#    import time
    
    ##Initialize
    Board = Board()
    start = Node(0, 0, 0, 0)
    end = Node(19, 19, 0, 0)
    open_list = [start] ##Pending tasks. Nodes that have been visited but neighbors have not been explored.
    closed_list = [] ##Nodes that have been visited and expanded.
    path = []
    
    ##Add obstacles
    for obs in obstacles:
        Board.addObstacle(obs)
    
    while (len(open_list) > 0):
        ##Consider the node with the lowest f score in the open list
        current = min(open_list)
        open_list.remove(current)
        
        ##Done
        if current == end:
            break
        
        closed_list.append(current)
        
        for neighbor in Board.getNeighbors(current):   
            neighbor_current_cost = current.g + current.getGScore(neighbor)
            if neighbor in open_list:
                if neighbor.g <= neighbor_current_cost:
                    continue
            elif neighbor in closed_list:
                if neighbor.g <= neighbor_current_cost:
                    continue
                closed_list.remove(neighbor)
                open_list.append(neighbor)
            else:
                open_list.append(neighbor)
                neighbor.h = neighbor.getHScore(end)
                    
            neighbor.g = neighbor_current_cost
            path.append((neighbor.y, neighbor.x))
    
    return path