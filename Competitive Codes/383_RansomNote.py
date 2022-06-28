#  WAY 1

class Solution:
    def ransomNote(self,ransomNote:str,magazine:str) -> bool:
        d = {}
        for item in magazine:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1

        for char in ransomNote:
            if char in d and d[char] > 0:
                d[char] -= 1
            else:
                return False
        return True

#  WAY 2

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t = list(magazine)

        for i in ransomNote:
            if i in t:
                t.remove(i)
                continue
            return False
        return True