from collections import deque

w, h = int(), int()
arr, visited = list(), list()
result = 0

d = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]

def bfs(x,y):
   global w, h, arr, result

   if not arr[x][y] or visited[x][y]:
      return

   queue = deque([(x, y)])
   result += 1
   
   while queue:
      dx, dy = queue.popleft()

      for i in range(8):
         nx, ny = dx + d[i][0], dy + d[i][1]

         if nx in range(h) and ny in range(w) and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx,ny))
   

def solution():
   global w, h, arr, result, visited

   while True:
      result = 0

      w,h = map(int, input().split())

      if w==h==0:
         break

      visited = [[False] * w for _ in range(h)]
      arr = [list(map(int, input().split())) for _ in range(h)]

      for x in range(h) :
         for y in range(w):
            bfs(x,y)

      print(result)

solution()