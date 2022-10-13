import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split(" "))

maze = []

for i in range(n):
   maze.append(list(map(int, input())))


print(maze)