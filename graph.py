#This is the graph api for the project
from collections import defaultdict
import pandas as pd

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def insertEdge(self, to,fromVertex):
        self.adj_list[to].append(fromVertex)
        if(fromVertex not in self.adj_list):
            self.adj_list[fromVertex] = []
    
    def hasEdge(self,to,fromVertex):
        if to not in self.adj_list or fromVertex not in self.adj_list:
            return false
        return fromVertex in self.adj_list[to]

    def djikstra(self):
        pass
    def bfs(self):
        pass
    