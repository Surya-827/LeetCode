class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()

        for i in nums1:
            if i in nums2:
                d[i] = min(nums1.count(i), nums2.count(i))
        x = list(set(nums1) & set(nums2))
        ans = []

        for i in x:
            if i in d.keys():
                for j in range(d[i]):
                    ans.append(i)
        return ans