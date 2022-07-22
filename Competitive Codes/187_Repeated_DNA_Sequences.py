class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        visited = set()
        for i in range(len(s) - 10 + 1):
            if s[i:i + 10] not in visited:
                visited.add(s[i:i + 10])
            else:
                print(s[i:i + 10])
                res.add(s[i:i + 10])
        return res
