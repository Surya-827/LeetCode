class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[None] * n for _ in range(n)]

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0
        count = 1
        for i in range(n ** 2):
            out[x][y] = count
            count += 1

            nx, ny = x + dir[d][0], y + dir[d][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or out[nx][ny] != None:
                d = (d + 1) % 4
                nx, ny = x + dir[d][0], y + dir[d][1]
            x, y = nx, ny
        return out