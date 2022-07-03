class Solution(object):

    def backtrack(self, nums):
        if (len(self.cur) == len(nums)):
            self.result.append(self.cur[:])
            return

        for i in range(len(nums)):
            if self.visited[i] == True:
                continue
            self.cur.append(nums[i])
            self.visited[i] = True
            self.backtrack(nums)
            self.cur.pop()
            self.visited[i] = False

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.visited = []
        for i in range(len(nums)):
            self.visited.append(False)
        self.cur = []

        self.backtrack(nums)

        return self.result