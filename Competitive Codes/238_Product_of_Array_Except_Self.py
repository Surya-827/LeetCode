
#WAY 1

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        res = [1] * (len(nums))
        for i in range(0, len(nums), 1):
            res[i] = temp
            temp = temp * nums[i]
        temp = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if i is 0:
                res[i] = temp
            else:
                res[i] = temp * res[i]
                temp = temp * nums[i]
        return res

#WAY 2
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach 1 Prefix and Suffix product in O(n) Space and Time
        n = len(nums)
        prefix_product = [1]*n
        suffix_product = [1]*n
        for i in range(1, n):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        for k in range(n-2, -1, -1):
            suffix_product[k] = suffix_product[k+1] * nums[k+1]   
        for i in range(0, n):
            nums[i] = prefix_product[i] * suffix_product[i]
        return nums
		#Runtime: 329 ms
		#Memory Usage: 22.6 MB

        # Approach 2 optimized O(1) Extra Space
        n = len(nums)
        output = [1]*n
        suffix_prod = 1 # variable to store suffix product till now
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        for i in range(n-1,-1, -1):
            output[i] = output[i] * suffix_prod
            suffix_prod = suffix_prod*nums[i]
        return output
"""