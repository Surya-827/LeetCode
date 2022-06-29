class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = {nums.pop(0): True}
        l = 1

        for n in nums:
            if n not in ret:
                ret[n] = True
                l += 1

        nums[:] = ret.keys()

        return l


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = [nums.pop(0)]
        last = ret[0]
        for n in nums:
            if n != last:
                ret.append(n)
                last = n

        nums[:] = ret

        return len(ret)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        n = 1
        length = len(nums)
        while n < length:
            if nums[n] == last:
                nums[:] = nums[:n] + nums[n + 1:]
                length = len(nums)
            else:
                last = nums[n]
                n += 1

        return len(nums)
        return len(nums)