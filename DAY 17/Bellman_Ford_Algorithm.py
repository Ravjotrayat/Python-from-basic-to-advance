#Find single source shortest path

from sys import maxsize

def BellmanFord(graph,v,e,src):
    dis=[maxsize]*v
    dis[src]=0
    for i in range(v-1):
        for j in range(e):
            if dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]]=dis[graph[j][0]]+graph[j][2]
                
    for i in range(e):
        x=graph[i][0]
        y=graph[i][1]
        weight=graph[i][2]
        if dis[x]!=maxsize and dis[x]+weight<dis[y]:
            print("Graph contains negative weights cycle")
    print("Vertex distance from source")
    for i in range(v):
        print(i,dis[i])

if __name__=="__name__":
    v=5
    e=8
    graph=[[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
    BellmanFord(graph,v,e,0)
