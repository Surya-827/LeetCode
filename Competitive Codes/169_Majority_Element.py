class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_val = len(nums) // 2
        count_map = {}
        for num in nums:
            if num not in count_map.keys():
                count_map[num] = 1
            else:
                count_map[num] += 1

        for k, v in count_map.items():
            if v > majority_val:
                return k