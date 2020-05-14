# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:06:23 2020

@author: nguye
"""
from tkinter import *
from a_star import solve

class App():
    def __init__(self, master):        
        
        self.master = master
        self.canvas = Canvas(master, bg="white", width=500, height=500)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 25
        self.cellheight = 25
        self.canvas.bind("<Button-1>", self.click)
        self.reset_button = Button(master, command = self.reset, text = "Reset grid")
        self.reset_button.pack(side = BOTTOM)
        self.start_button = Button(master, command = self.start, text = "Start A* path visualization")
        self.start_button.pack(side = BOTTOM)
       
        self.rect = {}
        for column in range(20):
            for row in range(20):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, \
                         fill="white", tags="rect")
                
    '''
        Add obstacles to the grid with a mouse click.
    
    '''
    def click(self, event):
        if self.canvas.find_withtag(CURRENT):
            self.canvas.after(5)
            self.canvas.itemconfig(CURRENT, fill="black")
    '''
       Fills canvas with path from A* 
    '''
    def start(self):
            
        ##Find obstacles
        obstacles = []
        for column in range(20):
            for row in range(20):
                if self.canvas.itemcget(self.rect[row, column], "fill") == "black":
                    obstacles.append((column, row))
                    
        ##Solve. Return path
        paths = solve(obstacles, self)
                
        ##Visualize Path
        for column in range(20):
            for row in range(20):
                if (row, column) in paths:
                    self.canvas.itemconfig(self.rect[row, column], fill="red")
                    print("path found", column, row)
        self.canvas.itemconfig(self.rect[0, 0], fill="green")
        self.canvas.itemconfig(self.rect[19, 19], fill="green")
#        
    '''
    
        Resets board to all white squares.
    '''
    def reset(self):
        for column in range(20):
            for row in range(20):
                self.canvas.itemconfig(self.rect[row, column], fill="white")
