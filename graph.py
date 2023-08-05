#This is the graph api for the project
from collections import defaultdict
import pandas as pd

class Graph:
    #The graph has one instance variable which is a default dictionary where keys have a empty list by defaultS
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    #Each word in the adjacency list stores their synonym which it is directed to in the graph
    #Uses the pseudocode from Module 8a by Amanpreet Kapoor
    def insertEdge(self,fromVertex,to):
        #So to is a synonyym of from and to is adjacent to from
        self.adj_list[fromVertex].append(to)
        if(to not in self.adj_list):
            self.adj_list[to] = []
    
    #Check if edge is present or in this case if to is a synonym of from
    def hasEdge(self,fromVertex,to):
        if to not in self.adj_list or fromVertex not in self.adj_list:
            return False
        return to in self.adj_list[fromVertex]

    def djikstra(self):
        pass
    def bfs(self):
        pass
    
