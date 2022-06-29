class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):  # define a function that will do the dfs for us
            area = 1  # since we have ATLEAST 1 piece, we will have this variable to 1
            grid[r][c] = 0  # we mark it as 0, as we don't want to visit this cell again in recursion
            paths = [(r - 1, c),
                     (r + 1, c),
                     (r, c - 1),
                     (r, c + 1)]  # possible paths one can traverse

            for row, col in paths:
                if (row >= 0 and row < len(grid) and  # check whether the row is in boundary condition
                        col < len(grid[0]) and col >= 0 and  # check whether column is in boundary condition
                        grid[row][col] == 1):  # check whether it is valid for us to search further or not
                    area += dfs(row, col)  # add the result we will obtain from other dfs

            return area

        max_area = float('-inf')  # to calculate the maximum area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == 1):  # we detected some land
                    max_area = max(max_area, dfs(r,
                                                 c))  # do a dfs search from here and try to find any other land which satisfies in our condition

        return max_area if max_area != float(
            '-inf') else 0  # if the ans is negative infinity, we couldn't find any land, hence return 0 