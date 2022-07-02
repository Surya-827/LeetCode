class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        nr, nc = len(grid), len(grid[0])
        rotten_oranges = deque([])
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        min_minutes = 0
        fresh_oranges = 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        while rotten_oranges:
            i, j, time = rotten_oranges.popleft()
            min_minutes = max(min_minutes, time)
            for di, dj in moves:
                x, y = i + di, j + dj
                if x >= 0 and x < nr and y >= 0 and y < nc and grid[x][y] == 1:
                    rotten_oranges.append((x, y, time + 1))
                    grid[x][y] = 2
                    fresh_oranges -= 1

        return min_minutes if fresh_oranges == 0 else -1