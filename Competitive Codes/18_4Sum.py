class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        ans = []
        while i < n-3:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            while j < n-2:
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                l = j+1
                r = n-1
                tasum = target - nums[i] - nums[j]

                while l < r:
                    if nums[l] + nums[r] == tasum:
                        ans.append([nums[i],nums[j],nums[l],nums[r] ])

                        while l < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1

                        l+=1
                        r-=1
                    elif nums[l] + nums[r] > tasum:
                        r-=1
                    else:
                        l+=1
                j+=1
            i+=1

        return(ans)