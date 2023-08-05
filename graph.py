#This is the graph api for the project
from collections import defaultdict
import pandas as pd
import time

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
    def bfs(self, fromVertex, to):
        start_time = time.time()
        #init a var for total nodes in graph
        n = len(self.adj_list)
        #init a queue
        q = []
        #add first node to queue
        q.append(fromVertex)
        #init a list of boolean values, all set to false to track visited nodes
        visited = [False]*n
        #set the start node’s visited status to True
        visited[fromVertex] = True
        #init a null list of size n to keep track of parent nodes used in queue
        prev = [-1]*n
        #init a flag to identify if 'to' node has been reached
        to_reached = False
        #while loop runs until queue is empty
        while len(q) > 0 and not to_reached:
            #dequeue the element from the front of the queue
            node = q.pop(0)
            neighbors = self.adj_list[node]

            for next_node in neighbors:
                if not visited[next_node]:
                    #enqueue the next node to the end of the queue
                    q.append(next_node)
                    visited[next_node] = True
                    prev[next_node] = node
                    if next_node == to:
                        to_reached = True
                        break

        # Filter out non -1 values of prev to get the shortest path
        shortest_path = [node for node in prev if node != -1]
        #append the to node to the end of the list since it wasnt included in the prev list
        shortest_path.append(to)
        #handle case where to vertex is unable to be reached: return -1 for minDist, 0 for execution time, and an empty list for shortest_path
        if len(shortest_path) == 0 or shortest_path[-1] != to:
            return -1, 0, []
        
        minPathDist = len(shortest_path)-1
        end_time = time.time()
        execution_time = end_time - start_time
        return minPathDist, execution_time, shortest_path
