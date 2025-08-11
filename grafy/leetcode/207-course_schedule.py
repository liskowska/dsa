"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that
you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

"""
==> szukanie cyklu w niespójnym grafie skierowanym
    - jest cykl -> return False
    - nie ma cyklu -> return True
    
żeby graf skierowany miał cykl, przechodząc przez graf dfs-em, wierzchołek musi być odwiedzony ponownie podczas
tej samej "wędrówki"
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
                if dfsCycle(G, u) is True: return False
    return True

# 1. case --> True
numCourses = 2
prerequisites = [[1,0]]

print(canFinish(numCourses, prerequisites))

# 2. case --> False
numCourses2 = 2
prerequisites2 = [[1,0],[0,1]]

print(canFinish(numCourses2, prerequisites2))