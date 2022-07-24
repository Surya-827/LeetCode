class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        oceans = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]

        def getNaighbour(row, col, heights):
            result = []
            if row > 0 and heights[row][col] <= heights[row - 1][col]:
                result.append([row - 1, col])
            if row < len(heights) - 1 and heights[row][col] <= heights[row + 1][col]:
                result.append([row + 1, col])
            if col > 0 and heights[row][col] <= heights[row][col - 1]:
                result.append([row, col - 1])
            if col < len(heights[0]) - 1 and heights[row][col] <= heights[row][col + 1]:
                result.append([row, col + 1])
            return result

        def dfs(row, col, heights, oceans, pacific, atlantic, result):
            if oceans[row][col][0] and pacific or oceans[row][col][1] and atlantic:
                return
            if (row == 0 or col == 0) and pacific:
                oceans[row][col][0] = True
            if (row == len(heights) - 1 or col == len(heights[0]) - 1) and atlantic:
                oceans[row][col][1] = True
            if pacific:
                oceans[row][col][0] = True
            else:
                oceans[row][col][1] = True

            neighbours = getNaighbour(row, col, heights)
            for r, c in neighbours:
                dfs(r, c, heights, oceans, pacific, atlantic, result)
            if oceans[row][col] == [True, True]:
                result.append([row, col])

        result = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                # For Pecific ocean
                if row == 0 or col == 0:
                    dfs(row, col, heights, oceans, True, None, result)
                # For Atlantic ocean
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    dfs(row, col, heights, oceans, None, True, result)
        return result