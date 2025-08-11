"""
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take
course bi first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
"""
from pydoc import visiblename

"""
Sprawdzam, czy przejscie jest mozliwe za pomoca canFinish z course schedule 1. Nastepnie sortowaniem topologicznym
ustalam kolejność kursów.
"""


def canFinish(numCourses, prerequisites):
    visited = [False for _ in range(numCourses)]
    cur_visited = [False for _ in range(numCourses)]

    def toList(G, n):
        list = [[] for _ in range(n)]
        for e1, e2 in G:
            list[e1].append(e2)
        return list

    def dfsCycle(G, v):
        def dfsVisit(G, v):
            visited[v] = True
            cur_visited[v] = True

            for u in G[v]:
                if cur_visited[u]: return True
                if not visited[u]:
                    if dfsVisit(G, u): return True

            cur_visited[v] = False
            return False

        for u in G[v]:
            if not visited[u]:
                if dfsVisit(G, u): return True
        return False

    G = toList(prerequisites, numCourses)
    for v in range(numCourses):
        for u in G[v]:
            if not visited[u]:
                if dfsCycle(G, u) is True: return False, G
    return True, G

def findOrder(numCourses, prerequisites):
    canI, G =  canFinish(numCourses, prerequisites)

    if not canI: return []

    def dfsTopoSort(G):
        n = len(G)
        visited = [False for _ in range(n)]
        sorted = []

        def dfsVisit(G, v):
            visited[v] = True
            for u in G[v]:
                if not visited[u]: dfsVisit(G, u)
            sorted.append(v)
            return

        for v in range(n):
            for u in G[v]:
                if not visited[v]: dfsVisit(G, v)

        return sorted

    sorted = dfsTopoSort(G)
    if len(sorted) != numCourses:
        for i in range(numCourses):
            if i not in sorted: sorted.append(i)
    return sorted

numCourses = 2
prerequisites = [[1,0]]
print(findOrder(numCourses, prerequisites))

numCourses2 = 4
prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses2, prerequisites2))

numCourses3= 1
prerequisites3 = []
print(findOrder(numCourses3, prerequisites3))
