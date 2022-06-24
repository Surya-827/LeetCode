from typing import List

class Solution:
    # @classmethod
    # def mergeSort(cls, arr: List[int], n: int) -> None:
    #     mid = n // 2
    #     L = arr[:mid]
    #     R = arr[mid:]
    #
    #     cls.mergeSort(L, len(L))
    #     cls.mergeSort(R, len(R))
    #
    #     left, right, idx = 0, 0, 0
    #
    #     while left < len(L) and right < len(R):
    #         if (L[left] < R[right]):
    #             arr[idx] = L[left]
    #             left += 1
    #         else:
    #             arr[idx] = R[right]
    #             right += 1
    #         idx += 1
    #
    #     while left < len(L):
    #         arr[idx] = L[left]
    #         idx += 1
    #         left += 1
    #
    #     while right < len(R):
    #         arr[idx] = R[right]
    #         right += 1
    #         idx += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Easy Way -Solution

        class Solution(object):
             def merge(self, nums1, m, nums2, n):
                 for i in range(n):
                   nums1[m+i]=nums2[i]
             return nums1.sort()
        """
        #Way - 2 Logic
        '''
        arr = []
        arr[:] = nums1[:m] + nums2[:n]
        self.mergeSort(arr, len(arr))
        print(arr)
        '''
        #Way - 3
        f_index = m+n-1
        left,right = m-1,n-1

        while left>=0 and right>=0:
            if(nums2[right] > nums1[left]):
                nums1[f_index] = nums2[right]
                right-=1
                f_index-=1
            else:
                nums1[f_index] = nums1[left]
                left-=1
                f_index-=1

        while left>=0:
            nums1[f_index] = nums1[left]
            left-=1
            f_index-=1

        while right>=0:
            nums1[f_index] = nums2[right]
            right-=1
            f_index-=1
        print(nums1)



if __name__=="__main__":

    nums1 = list(map(int,input().split()))#[1,2,3,0,0,0]
    m = int(input())#3
    nums2 = list(map(int,input().split()))#[2,5,6]
    n = int(input())#3
    s = Solution()
    s.merge(nums1,m,nums2,n)

