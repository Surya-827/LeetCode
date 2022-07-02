class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =[]
        hashmap = {}
        stack = []
        for num in nums2:
            while len(stack) != 0 and num > stack[-1]:
                temp = stack.pop()
                hashmap[temp] = num
            stack.append(num)
        while len(stack)!=0:
            temp = stack.pop()
            hashmap[temp] = -1
        for num in nums1:
            if num in hashmap:
                result.append(hashmap[num])
        return result