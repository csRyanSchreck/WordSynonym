#This is the graph api for the project
from collections import defaultdict
import pandas as pd
import time
from queue import PriorityQueue
import sys
import heapq

#This is the class that is used to create a adjacency list and contain functions to determine the minimum path
class Graph:
    #constructor creates a default dictionary which contains empty list
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    #The insert edge function will append the dest vertex into the list that is associated with the fromVertex
    #This essentialy creates a directed edges for fromVertex->to where the edge represents that to is a synonym of fromVertex
    def insertEdge(self,fromVertex,to):
        self.adj_list[fromVertex].append(to)
        if(to not in self.adj_list):
            self.adj_list[to] = []
    
    #This function will check if to is adjacent to fromVertex or in our program's contex if to is a synonym of fromVertex
    def hasEdge(self,fromVertex,to):
        if to not in self.adj_list or fromVertex not in self.adj_list:
            return False
        return to in self.adj_list[fromVertex]
    
    #This is the dijkstra algorithm to compute the minimum path 
    #This function returns three different output: the minimum path or error message, the time to compute, and the nodes in the minimum path
    def dijkstra(self,fromNode,toNode):
        start_time = time.time()

        #Check if the words exist
        if(fromNode not in self.adj_list or toNode not in self.adj_list):
            if toNode not in self.adj_list:
                return "Error: "+toNode+" is not valid",time.time()-start_time,[]
            else:
                return "Error: "+fromNode+" is not valid",time.time()-start_time,[]
      
        # Initialize dictionary to have infinity for every value
        distances = {node: float('inf') for node in self.adj_list.keys()}

        #Dictionary for holding previous node
        parent = {}
        for node in self.adj_list.keys():
            parent[node] = ""
        
        #set the fromNode distance to 0
        distances[fromNode] = 0
    
        # Initialize list of nodes to pass through starting with the fromNode
        notDoneNode = [(fromNode, 0)]
        
        while notDoneNode:
            # returns smallest weight
            node, weight = heapq.heappop(notDoneNode)
          
            # iterates through all adjacent nodes of current node
            for adjacentNode in self.adj_list[node]:
                totalWeight = weight + 1
                if distances[adjacentNode] > totalWeight:
                    distances[adjacentNode] = totalWeight
                    parent[adjacentNode]=node
                    remove=-1
                    #This code is to check if the vertex already exists in the priority queue and if it does then we need to remove it
                    for i in range(len(notDoneNode)):
                        if notDoneNode[i][0]==adjacentNode:
                            remove=i
                            break
                    if remove!=-1:
                        notDoneNode[remove]=notDoneNode[-1]
                        notDoneNode.pop()
                        heapq.heapify(notDoneNode)
                    #Once the data is no longer in the priority queue we can add it again 
                    heapq.heappush(notDoneNode, (adjacentNode, totalWeight))

        #returns only the path between from and to node
        orderList = []
        tempNode = parent[toNode]
        orderList.append(tempNode)
        while True:
            if tempNode =='':
                break
            tempNode = parent[tempNode]
            orderList.append(tempNode)
        orderList.pop()

        #Reverse the order of the nodes and add to the end the destination node
        orderList.reverse()
        orderList.append(toNode)
    
        #Get the minimum weight
        minWeight = len(orderList) - 1
        finalTime = time.time()
        
        return minWeight if minWeight!=0 else "No path exists",round(finalTime-start_time,4),orderList if minWeight!=0 else []
    
    #BFS algorithm that gets the minimum path for the from to the to vertex
    #This function returns three different output: the minimum distance or a error message, the time to compute, and the nodes in the minimum path
    def bfs(self, fromVertex, to):
        start_time = time.time()
        #Check if the words exist
        if(fromVertex not in self.adj_list or to not in self.adj_list):
            if to not in self.adj_list:
                return "Error: "+to+" is not valid",time.time()-start_time,[]
            else:
                return "Error: "+fromVertex+" is not valid",time.time()-start_time,[]

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
        execution_time = round(end_time - start_time, 4)
        return minPathDist, execution_time, shortest_path
