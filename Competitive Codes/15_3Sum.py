import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target: could be changed into any numbers -> a + b + c == target
        target = 0
        # smaller: numbers which is not larger than target // 3
        smaller = set()
        # larger: numbers which is larger than target // 3
        larger = set()
        checker = collections.defaultdict(int)
        output = set()
        for num in nums:
            checker[num] += 1
            # Group numbers by comparing with target // 3
            smaller.add(num) if num <= target // 3 else larger.add(num)

        # choose one number from each group.
        for smallNum in smaller:
            for largeNum in larger:
                remain = target - smallNum - largeNum
                # Find if there is a number [remain] that matches [remain + smallNum + largeNum = target]
                # Be careful with cases including duplicate numbers. eg. [-1, -1, 2], [-2, 1, 1]
                if remain in checker and (remain != smallNum or checker[smallNum] > 1) and (
                        remain != largeNum or checker[largeNum] > 1):
                    output.add(tuple(sorted([remain, smallNum, largeNum])))
        # Add case in triplicate numbers.
        if target % 3 == 0 and checker[target // 3] >= 3:
            output.add((target // 3, target // 3, target // 3))
        return output


# Solution
# using
# sort and two
# pointers
# instead
# of
# make
# set
# for small numbers and large numbers:


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target could be changed into any numbers -> a + b + c == target
        target = 0
        checker = collections.Counter(nums)
        sortedNums = sorted(checker.keys())
        output = set()
        i = 0
        # sortedNums[i]: A number not larger than target // 3
        # sortedNums[j]: A number larger than target // 3
        while i < len(sortedNums) and sortedNums[i] <= target // 3:
            j = len(sortedNums) - 1
            while j > i and sortedNums[j] > target // 3:
                remain = target - sortedNums[i] - sortedNums[j]
                if remain in checker and (checker[remain] > 1 or (remain != sortedNums[i] and remain != sortedNums[j])):
                    output.add(tuple(sorted([remain, sortedNums[i], sortedNums[j]])))
                j -= 1
            i += 1
        # Add case in triplicate numbers.
        if target % 3 == 0 and checker[target // 3] >= 3:
            output.add((target // 3, target // 3, target // 3))
        return output