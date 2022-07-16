class Solution:
    def deleteAndEarn(self, nums):
        cnt = Counter(nums)
        dp = [0, 0]
        temp = -1

        for num in sorted(cnt):
            if num != temp + 1:
                dp.append(dp[-1] + num * cnt[num])
            else:
                dp.append( max( dp[-2] + num * cnt[num], dp[-1]))
            temp = num

        return dp[-1]