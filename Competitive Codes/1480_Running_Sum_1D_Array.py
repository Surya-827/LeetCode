from typing import List

class Solution(object):

    @classmethod
    def runningSum(self,nums : List[int]) -> List[int]:
        """
        :param nums:
        :return:
        """
        res = [nums[0]]

        for i in range(1,len(nums)):
            nums[i] = nums[i-1]+nums[i]
            res[i]+=[nums[i]]
        return res


if __name__=="__main__":

    obj = Solution()
    arr = list(map(int,input().split()))
    n = len(arr)

    print(obj.runningSum(arr))