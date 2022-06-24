from typing import List
from pyparsing import nums

class Solution:
	@classmethod
	def rotateArray(cls,nums:List[int],k:int) -> None:
		'''
		:param nums:
		:param k:
		:return:
		'''
# WAY - 1
# 		if k % len(nums) != 0 and len(nums) > 1:
# 			nums[:] = nums[-k % len(nums):] + nums[:len(nums) - k % len(nums)]

# WAY - 2
# 	    if k > len(nums):
# 			k%=len(nums)
# 		nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]


if __name__=="__main__":
    arr = list(map(int,input().split()))
    k=int(input())
    ans = Solution()
    ans.rotateArray(arr,k)


