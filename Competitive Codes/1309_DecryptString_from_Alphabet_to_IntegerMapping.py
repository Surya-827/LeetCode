#WAY 1 Using Dictionary

class Solution:
	def freqAlphabets(self, s: str) -> str:

		d = {'1':'a','2':'b','3':'c','4':'d','5':'e',
			 '6':'f','7':'g','8':'h','9':'i','10#':'j',
			 '11#':'k','12#':'l','13#':'m','14#':'n',
			 '15#':'o','16#':'p','17#':'q','18#':'r',
			 '19#':'s','20#':'t','21#':'u','22#':'v',
			 '23#':'w','24#':'x','25#':'y','26#':'z'}

		result = ''
		i = 0

		while i < len(s):
			if s[i:i+3] in d:
				result = result + d[s[i:i+3]]
				i = i + 3
			elif s[i] in d:
				result = result + d[s[i]]
				i = i + 1
		return result

	
# WAY 2 Using Asciii

class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                n = int(s[i-2] + s[i-1])
                res = chr(96+n) + res
                i -= 3
            else:
                res = chr(96+int(s[i])) + res
                i -= 1
        return res