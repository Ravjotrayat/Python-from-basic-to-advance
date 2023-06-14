'''
Algorithm for Djiktras
1.) Create a set sptSet (shortest path tree set) that keeps track of
vertices included in the shortest path tree, i.e.,
whose minimum distance from the source is calculated and finalized.
Initially, this set is empty.

2.) Assign a distance value to all vertices in the input graph. Initialize
all distance values as INFINITE. Assign the distance value as 0
for the source vertex so that it is picked first.

3.) While sptSet doesn’t include all vertices 
Pick a vertex u that is not there in sptSet and has a minimum distance
value. 
Include u to sptSet.
Then update the distance value of all adjacent vertices of u. 
To update the distance values, iterate through all adjacent vertices. 
For every adjacent vertex v, if the sum of the distance value of
u (from source) and weight of edge u-v, is less than the distance value
of v, then update the distance value of v.

'''

class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph= [ [ 0 for column in range(vertices)]
                     for row in range(vertices)]
    def printSolution(self,dist):
        print("Vertex \t Distance from Source")
        for node in range (self.v):
            print(node,"\t\t",dist[node])

    def minDistance(self,dist,sptSet):
        min=1e7
        for i in range(self.v):
            if dist[i] < min and sptSet[i]==False:
                min=dist[i]
                min_index=i
        return min_index

    def dijkstra(self,src):
        dist=[1e7]*self.v
        dist[src]=0
        sptSet=[False]*self.v
        for cout in range(self.v):
            u=self.minDistance(dist,sptSet)
            sptSet[u]=True
            for j in range(self.v):
                if self.graph[u][j]>0 and sptSet[j] ==False and  dist[j]>dist[u]+self.graph[u][j]:
                    dist[j]=dist[u]+self.graph[u][j]
        self.printSolution(dist)
g=Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
         [4,0,8,0,0,0,0,11,0],
         [0,8,0,7,0,4,0,0,2],
         [0,0,7,0,9,14,0,0,0],
         [0,0,0,9,0,10,0,0,0],
         [0,0,4,14,10,0,2,0,0],
         [0,0,0,0,0,2,0,1,6],
         [8,11,0,0,0,0,1,0,7],
         [0,0,2,0,0,0,6,7,0]]
g.dijkstra(0)
        
                    
        


        
