from collections import deque
import queue
from tkinter.tix import Tree

INF = 999999999

graph = [
   [0, 7, 5],
   [7, 0, INF],
   [5, INF, 0]
]

graph_adj = [[] for _ in range(3)]

graph_adj[0].append((1,7))
graph_adj[0].append((2,5))
graph_adj[1].append((0,7))
graph_adj[2].append((0,5))

graph_dfs = [
   [],
   [2, 3, 8],
   [1, 7],
   [1, 4, 5],
   [3, 5],
   [3, 4],
   [7],
   [2, 6, 8],
   [1, 7]
]

visited = [False] * 9

def dfs(graph_dfs, v, visited):
   visited[v] = True
   print(v, end = ' ')

   for i in graph_dfs[v]:
      if not visited[i]:
         dfs(graph_dfs, i, visited)


#dfs(graph_dfs, 1, visited)

def bfs(graph, start, visited):
   queue = deque([start])
   visited[start] = True
   while queue:
      v = queue.popleft()
      print(v, end = ' ')

      for i in graph[v]:
         if not visited[i]:
            queue.append(i)
            visited[i] = True

bfs(graph_dfs, 1, visited)

