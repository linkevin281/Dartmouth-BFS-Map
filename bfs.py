# name: Kevin Lin
# date: 03/11/21
# purpose: create Breadth-first search with backchaining

from collections import *

# Parameters: start and goal are vertex objects
# performs a Breadth-first search and returns a list of the shortest path from goal to start vertexes
def bfs(start, goal):
    frontier = deque()
    backpointer = {}

    frontier.append(start)
    backpointer[start] = "None"

    while frontier:
        v = frontier.popleft()
        for i in v.adj_list:
            if i not in backpointer:
                frontier.append(i)
                backpointer[i] = v
            if i == goal:
                break
    x = goal
    path = []

    while x != "None":
        path.append(x)
        x = backpointer[x]

    return path