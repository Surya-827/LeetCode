class Solution:
    def search(self, nums: List[int], target: int) -> int:
        num=sorted(nums)
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        try:
            return dic[target]
        except:
            return -1