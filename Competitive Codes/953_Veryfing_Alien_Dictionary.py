class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = {char:i for i,char in enumerate(order)}
        for idx in range(1,len(words)):
            prev,current,correctOrder = words[idx-1], words[idx], False
            for i in range(min(len(prev), len(current))):
                if alphabets[prev[i]] < alphabets[current[i]]:
                    correctOrder = True
                    break
                if alphabets[prev[i]] > alphabets[current[i]]:
                    return False
            if not correctOrder and len(prev) > len(current):
                return False
        return True