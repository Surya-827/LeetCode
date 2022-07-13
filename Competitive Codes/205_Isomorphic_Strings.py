
#WAY 1

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = True
        mapS = {} # s-char : t-char
        mapT = {} # t-char : s-char

        for i, char in enumerate(s):
            if char not in mapS and t[i] not in mapT:
                mapS[char] = t[i]
                mapT[t[i]] = char
            elif char in mapS and mapS[char] == t[i]:
                continue
            elif t[i] in mapT and mapT[t[i]] == char:
                continue
            else:
                iso = False

        return iso


#wAY 2

class Solution:
    def check(self, str1,str2, _dict, i):
        litter_in_dict = _dict.get(str1[i], None)
        if litter_in_dict:
            if litter_in_dict != str2[i]:
                return False
            return True
        else:
            _dict[str1[i]] = str2[i]
            return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        sLength = len(s)
        for i in range(sLength):
            if not self.check(s, t, dict1, i):
                return False
            if not self.check(t, s, dict2, i):
                return False

        return True