# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:08:01 2020

@author: nguye
"""


##Start A* Algorithm**
def solve(obstacles):
    from node import Node
    from board import Board
    ##Initialize
    Board = Board()
    start = Node(0, 0, 0, 0)
    end = Node(39, 39, 0, 0)
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
#        print("Current:", current.x, current.y)
        
        ##Done
        if current == end:
            path.append((19, 19))
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
            path.append((neighbor.x, neighbor.y))
    
    return path