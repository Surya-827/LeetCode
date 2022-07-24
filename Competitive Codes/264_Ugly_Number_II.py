#WAY 1 Using DP

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        c2 = 1
        c3 = 1
        c5 = 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = min(2 * dp[c2], 3 * dp[c3], 5 * dp[c5])

            if dp[i] == 2 * dp[c2]:
                c2 += 1
            if dp[i] == 3 * dp[c3]:
                c3 += 1
            if dp[i] == 5 * dp[c5]:
                c5 += 1

        return dp[n]

#WAY 2
def nthUglyNumber(self, k: int) -> int:
    res=[1]
    i2=i3=i5=0
    while(len(res)<k):
        m2=2*res[i2]
        m3=3*res[i3]
        m5=5*res[i5]
        minimum=min(m2,m3,m5)
        res.append(minimum)
        if(minimum==m2):
            i2+=1
        if(minimum==m3):
            i3+=1
        if(minimum==m5):
            i5+=1
    return res[k-1]