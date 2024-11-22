def floyd_warshell(graph):
    n=len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    return graph
graph = [
    [0, 3, float('inf'), float('inf')],
    [2, 0, float('inf'), 1],
    [float('inf'), 7, 0, 2],
    [6, float('inf'), 3, 0]
]
for row in floyd_warshell(graph):
    print(row)
   
