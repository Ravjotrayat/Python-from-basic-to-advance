class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[]

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

        #searching is the next step

    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])

    def apply_union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] =yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
            
    def kruskal_algo(self):
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key=lambda item:item[2])
        parent=[]
        rank=[]
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        while e<self.v-1:
            u,v,w=self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e+=1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
        for u,v,weight in result:
            print("%d - %d - %d"%(u,v,weight))
s=Graph(6)
s.add_edge(0,1,4)
s.add_edge(0,2,4)
s.add_edge(1,2,2)
s.add_edge(1,0,4)
s.add_edge(2,1,2)
s.add_edge(2,0,4)
s.add_edge(2,4,4)
s.add_edge(2,3,3)
s.add_edge(2,5,2)
s.add_edge(5,2,2)
s.add_edge(3,4,3)
s.add_edge(4,2,4)
s.add_edge(4,5,3)
s.add_edge(4,3,3)
s.add_edge(5,4,3)

s.kruskal_algo()

        
            
        
        
