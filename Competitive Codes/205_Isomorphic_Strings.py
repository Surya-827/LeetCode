class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        comprasion_dict = {}

        for i in range(len(s)):
            if comprasion_dict.get(s[i]):
                if comprasion_dict[s[i]] != t[i]:
                    return False
            else:
                comprasion_dict[s[i]] = t[i]

        return len(comprasion_dict.values()) == len(set(comprasion_dict.values()))