#This is the graph api for the project
from collections import defaultdict
import pandas as pd

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def insertEdge(self,fromVertex,to):
        self.adj_list[fromVertex].append(to)
        if(to not in self.adj_list):
            self.adj_list[to] = []
    
    def hasEdge(self,fromVertex,to):
        if to not in self.adj_list or fromVertex not in self.adj_list:
            return False
        return to in self.adj_list[fromVertex]

    def djikstra(self):
        pass
    def bfs(self):
        pass
    
