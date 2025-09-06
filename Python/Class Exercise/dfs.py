def DFS(graph, start) :
    visited = set() #keep track visited nodes
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node) # track the nide as visited
            print(node, end=' ')
            stack.extend(graph[node])

# Create the adjacency list to represent the graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}

DFS(graph, 'A')