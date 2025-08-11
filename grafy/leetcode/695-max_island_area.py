"""
695. Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 on the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
from collections import deque

def maxAreaOfIsland(grid):
    if not grid: return 0

    n = len(grid[0])
    m = len(grid)

    visited = [[False for _ in range(n)] for _ in range(m)]

    max_area = 0

    def bfs(r, c):
        cur_area = 1
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        Q = deque()
        visited[r][c] = True
        Q.append((r, c))

        while Q:
            row, column = Q.popleft()
            for dr, dc in directions:
                if((dr+row) in range(m) and
                (dc+column) in range(n) and
                grid[dr+row][dc+column] == 1 and
                 not visited[dr+row][dc+column]):
                    Q.append((dr+row, dc+column))
                    visited[dr+row][dc+column] = True
                    cur_area += 1
        return cur_area

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and not visited[r][c]:
                area = bfs(r, c)
                if area > max_area: max_area = area

    else: return max_area

grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0]]

print(maxAreaOfIsland(grid1))

