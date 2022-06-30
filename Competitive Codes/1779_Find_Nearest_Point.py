class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        for i, point in enumerate(points):
            cur_dist = -1
            if point[0] == x:
                cur_dist = abs(y - point[1])
            if point[1] == y:
                cur_dist = abs(x - point[0])
            if cur_dist == -1:  # Point isn't valid
                continue
            if index == -1:  # First valid point
                min_dist = cur_dist
                index = i
            else:
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    index = i
        return index