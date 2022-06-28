from itertools import permutations as p

# WAY 1
# just in case, you know..
#if len(s2) < len(s1): return False

# useful shit
# f1, f2 = [0]*26, [0]*26
# atoi = lambda x: ord(x)-97
#
# # init frequencies
# for c in s1: f1[atoi(c)] += 1
# for c in s2[:len(s1)]: f2[atoi(c)] += 1
#
# # sliding window
# if f1 == f2: return True
# for i in range(len(s1), len(s2)):
# 	f2[atoi(s2[i-len(s1)])] -= 1
# 	f2[atoi(s2[i])] += 1
# 	if f1 == f2: return True
#
# return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        h2 = [0] * 26
        h1 = [0] * 26

        for c in s1:
            h1[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            if i < n:
                h2[ord(s2[i]) - ord('a')] += 1
            else:
                h2[ord(s2[i]) - ord('a')] += 1
                h2[ord(s2[i - n]) - ord('a')] -= 1

            if h1 == h2: return True

        return False


if __name__=="__main__":

    obj = Solution()

    s1="ab"
    s2="eidboaoo"
    print(obj.checkInclusion(s1,s2))