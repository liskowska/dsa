"""
Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water),
return the number of islands.
"""
from collections import deque
from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows = len(grid)
        columns = len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        islands = 0

        def bfs(r, c):
            Q = deque()
            visited[r][c] = True
            Q.append((r, c))

            while Q:
                cr, cc = Q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:

                    if ((cr + dr) in range(rows) and
                            (cc + dc) in range(columns) and
                            grid[cr + dr][cc + dc] == "1" and
                            not visited[cr + dr][cc + dc]):
                        Q.append((cr + dr, cc + dc))
                        visited[cr + dr][cc + dc] = True
            return

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    islands += 1
        return islands


grid1 = [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]

grid2 = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]

