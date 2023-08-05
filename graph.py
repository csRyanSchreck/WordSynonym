#This is the graph api for the project
from collections import defaultdict
import pandas as pd
import time
from queue import PriorityQueue
import sys
import heapq
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

    def djikstra(self,fromVertex,to):
        start_time = time.time()
        if(fromVertex not in self.adj_list or to not in self.adj_list):
            return "Error: one of your words is not valid",time.time()-start_time,[]
        q = PriorityQueue()
        q.put((0,fromVertex))
        p={}
        d={}
        for key in self.adj_list:
            if key!=fromVertex:
                q.put((float('inf'), str(key)))
                d[key]=float('inf')
            else:
                d[key]=0
            p[key]=-1

        while q.empty() is False:
            prio,top = q.get()
            if prio==float('inf'):
                break
            for vertex in self.adj_list[top]:
                if d[top]+1<d[vertex]:
                    q.queue.remove((d[vertex],vertex))
                    d[vertex]=d[top]+1
                    q.put((d[vertex],vertex))
                    p[vertex]=top
        if d[to]!=float('inf'):
            path=[]
            vertex=to
            while vertex!=fromVertex:
                path.append(vertex)
                vertex = p[vertex]
            path.append(vertex)
            path.reverse()
        else:
            path=[]
        end_time = time.time()  
        return "Error not connected" if d[to]==float('inf') else d[to],round(end_time-start_time),path
           
    def bfs(self, fromVertex, to):
        start_time = time.time()
        #Check if the words exist
        if(fromVertex not in self.adj_list or to not in self.adj_list):
            return "Error: one of your words is not valid",time.time()-start_time,[]

        #init a map of vertexes and their associated indices: keys are vertexs, values are indices
        vertex_to_index = {vertex: index for index, vertex in enumerate(self.adj_list.keys())}
        #init var for both the fromVertex index and the to vertex and set them equal to their mapped values(indices)
        fromVertexIndex = vertex_to_index[fromVertex]
        toIndex = vertex_to_index[to]

        #init a var for total nodes in graph
        n = len(self.adj_list)
        #init a queue
        q = []
        #add first node to queue
        q.append(fromVertexIndex)
        #init a list of boolean values, all set to false to track visited nodes
        visited = [False]*n
        #set the start node’s visited status to True
        visited[fromVertexIndex] = True
        #init a null list of size n to keep track of parent nodes used in queue
        prev = [-1]*n
        #init a flag to identify if 'to' node has been reached
        to_reached = False
        #while loop runs until queue is empty
        while len(q) > 0 and not to_reached:
            #dequeue the element from the front of the queue
            node = q.pop(0)
            neighbors = self.adj_list[list(self.adj_list.keys())[node]]

            for next_node in neighbors:
                next_node_index = vertex_to_index[next_node]
                if not visited[next_node_index]:
                    #enqueue the next node to the end of the queue
                    q.append(next_node_index)
                    visited[next_node_index] = True
                    prev[next_node_index] = node
                    if next_node == to:
                        to_reached = True
                        break

        #init a list of shortest_path_indices
        shortest_path_indices = []
        node = toIndex
        #iterate through the prev list of parent nodes and populate into shortest path list of indices
        while node != -1:
            shortest_path_indices.insert(0, node)
            node = prev[node]

        #init a list of the strings of vertexes in the shortest path
        shortest_path = [list(vertex_to_index.keys())[index] for index in shortest_path_indices]
        #handle case where to vertex is unable to be reached: return -1 for minDist, 0 for execution time, and an empty list for shortest_path
        if not to_reached:
            return "No path exists", 0, []
        
        minPathDist = len(shortest_path) - 1
        end_time = time.time()
        execution_time = end_time - start_time
        return minPathDist, execution_time, shortest_path
