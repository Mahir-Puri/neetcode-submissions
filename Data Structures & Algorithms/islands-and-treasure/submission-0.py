
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # Step 1: Add all treasure chests to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0

        # Step 2: BFS starting from all treasure chests
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visit):

                        q.append((nr, nc))
                        visit.add((nr, nc))

            dist += 1
