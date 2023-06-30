'''
Formula: Staring from 1
g(i,{2,3,4})=min {c1 to any k+g(k,{2,3,4}-{k})}
general formula :
g(i,s)=min{CiK+G(K,S-{K})}

'''
from sys import maxsize
from itertools import permutations
v=4
#implementing of traveling Salesman Problem..
def travellingSalesmanProblem(graph,s):
    vertex =[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=graph[k][s]
        min_path=min(min_path,current_pathweight)

    return min_path
if __name__=="__main__":
    #graph=[[10,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    graph=[[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
    s=0
    print(travellingSalesmanProblem(graph,s))
        
