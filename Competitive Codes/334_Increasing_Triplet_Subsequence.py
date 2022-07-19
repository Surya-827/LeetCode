class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        # We only need to keep the smallest number and the least amount we need to shape a triplet.
        # This way, when we get to a number, we can compre it with the smallest number up until now, or see if it is the last element of a triplet.
        # time: O(n)
        # space: O(1)
        smallest_number = nums[0]
        smallest_number_to_triplet = float("inf")

        for num in nums:
            if num > smallest_number_to_triplet:
                return True
            if num < smallest_number:
                smallest_number = num
            elif num > smallest_number:
                smallest_number_to_triplet = num

        return False