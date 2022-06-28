from typing import List

class Solution(object):
    def findMedian(self,nums1:List[int],nums2:List[int]) -> float:
        size = len(nums1) + len(nums2)
        mid = 0
        nums1.extend(nums2)
        nums1.sort()

        if(size%2==0):
            mid = (nums1[size//2-1]+nums1[size//2])//2
        else:
            mid = size//2
        return float(mid)


if __name__=="__main__":

    obj = Solution()
    x = list(map(int,input().split()))#[1,2]
    y = list(map(int,input().split()))#[3,4]
    print(obj.findMedian(x,y))