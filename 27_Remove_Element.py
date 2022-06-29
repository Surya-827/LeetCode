class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        while(n <= len(nums) - 1):
            if nums[n] == val:
                nums.pop(n)
                n = n - 1
            n = n + 1
        return len(nums)