

Graph = []


Graph.append([1,3])
Graph.append([3])
Graph.append([1,3])
Graph.append([4])
Graph.append([])





def dfs(at, visited, visitedVerteces, Graph):
    visited[at] = 1
    for vertex in Graph[at]:
        if not visited[vertex]:
            dfs(vertex,visited, visitedVerteces, Graph)
    visitedVerteces.append(at)


def topsort(Graph):
    V = len(Graph)
    visited = [0] * V
    order = [0]*V
    i = V-1
    for at in visited:
        if not at:
            visitedVerteces = []
            dfs(at, visited, visitedVerteces, Graph)
            for vertex in visitedVerteces:
                order[i] = vertex
                i-=1


    return order

print(topsort(Graph))