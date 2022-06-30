
#WAY 1
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ""
        prefix = min(strs, key=len)
        for i in range(0, len(prefix)):
            q = prefix[:i+1]
            has_all = True
            for s in strs:
                if not s.startswith(q):
                    has_all = False
                    break
            if has_all == False:
                return q[:i]
        return prefix


#WAY 2
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		smallest_str = min(strs, key=len)
		for i, v in enumerate(smallest_str):
			for let, L in zip(cycle(v), strs):
				if let != L[i]: return smallest_str[:i]
		return smallest_str