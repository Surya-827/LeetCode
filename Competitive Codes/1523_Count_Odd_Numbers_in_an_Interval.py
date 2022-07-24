#WAY 1 Using Math

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        edges = (high%2) + (low%2)
        middle = math.floor((high-low-1)/2)
        return edges + middle + 1 if edges == 0 else edges + middle


# Way 2 Using Anonymous Function
