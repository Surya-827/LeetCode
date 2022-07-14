#WAY 1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        x=sum(nums)
        left=0
        right=x
        for i in range(0,len(nums)):
            if(i>0):
                left+=nums[i-1]
            right-=nums[i]
            if(left==right):
                return i
        return -1

#WAY 2
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)

        for i in range(1, length):
            nums[i] += nums[i - 1]

        def isPivot(index):
            if index == 0:
                return nums[-1] - nums[index] == 0
            if index == length - 1:
                return nums[index - 1] == 0
            return nums[index - 1] == nums[-1] - nums[index]

        for i in range(length):
            if isPivot(i):
                return i

        return -1