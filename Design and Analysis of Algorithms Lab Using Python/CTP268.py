# Q13 (answer updated)

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	if v not in graph[u]:
		graph[u].append(v)
	if u not in graph[v]:
		graph[v].append(u)
	        
start_vertex = int(input())
	        
def bfs(graph, start_vertex):
	visited = [False] * len(graph)
	queue = [start_vertex]
	        	            
	while queue:
		vertex = queue.pop(0)
		if not visited[vertex]:
			print(vertex, end=' ')
			visited[vertex] = True
			for neighbor in sorted(graph[vertex]):
				if not visited[neighbor]:
					queue.append(neighbor)
bfs(graph, start_vertex)
