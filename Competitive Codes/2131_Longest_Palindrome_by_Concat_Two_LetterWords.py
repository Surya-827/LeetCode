class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        C = Counter(words)
        C2 = C.copy()

        V, out = set(), 0

        for k, v in C.items():

            if k[0] == k[1]:  # found aa, pair them up if they are more than 1 of them
                out += C2[k] // 2 * 4
                C2[k] -= C2[k] // 2 * 2
                if C2[k]:  # if left over add them to V so we can revisit them later
                    V.add(k)

            else:
                rem = k[1] + k[0]
                if rem in V:
                    kV, remV = C2[k], C2[rem]
                    out += min(kV, remV) * 4  # number of pairs * 4
                    C2[k] -= min(kV, remV)  # modify the remaining words frequencies
                    C2[rem] -= min(kV, remV)  # modify the remaining words frequencies
                    V.remove(rem)  # remove paird V
                else:
                    V.add(k)

        for word in V:
            if word[0] == word[1]:
                return out + 2
        return out 