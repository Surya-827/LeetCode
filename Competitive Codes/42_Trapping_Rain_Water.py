class Solution:
    def trap(self, height: List[int]) -> int:
        start,end = 0, len(height)-1
        res = 0
        waterincell = []
        for i in range(len(height)):
            if height[start] < height[i] :
                start = i
            waterincell.append(height[start] - height[i])
        for i in range(len(height)-1,-1,-1):
            if height[end] < height[i] :
                end = i
            res += min((height[end] - height[i]), waterincell[i])
        return res