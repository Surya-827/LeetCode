
#WAY 1
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        i=0
        while(i<n):
            j=i
            while(j<n):
                ans+=sum(arr[i:j+1])
                j+=2
            i+=1
        return ans


#WAY 2
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        times = (n + 1) // 2  # occurrence times
        count = 0
        for i in range(n):
            mi = min(i + 1, n - i)  # min distance
            ltimes = mi // 2  # left edges
            count += ((ltimes) ** 2) * arr[i]
            if (n % 2 == 1):
                rtimes = mi // 2
                count += ((mi // 2) ** 2) * arr[i]
            elif (n % 2 == 0):
                rtimes = ((mi - 1) // 2)
                count += (rtimes * (rtimes + 1)) * arr[i]
            count += (times - ltimes - rtimes) * mi * arr[i]

        return count