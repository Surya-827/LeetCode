class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        points = set()
        points.add((sr, sc))
        old_color = image[sr][sc]
        if color == old_color: return image
        rows = len(image) - 1
        cols = len(image[0]) - 1

        def get_new_points():
            new_points = set()
            for sr, sc in points:
                if sc < cols:
                    if image[sr][sc + 1] == old_color:
                        new_points.add((sr, sc + 1))

                if sc > 0:
                    if image[sr][sc - 1] == old_color:
                        new_points.add((sr, sc - 1))

                if sr > 0:
                    if image[sr - 1][sc] == old_color:
                        new_points.add((sr - 1, sc))

                if sr < rows:
                    if image[sr + 1][sc] == old_color:
                        new_points.add((sr + 1, sc))

            return (new_points)

        while points:
            for x, y in points:
                image[x][y] = color
            points = get_new_points()

        return image