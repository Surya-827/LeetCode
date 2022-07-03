#WAY 1

class Solution(object):

    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.res = []

        def backtrack(s, st="", i=0):
            if len(st) == len(s):
                self.res.append(st)
                return

            if i >= len(s):
                return

            if s[i].isalpha():
                backtrack(s, st + s[i].swapcase(), i + 1)
            backtrack(s, st + s[i], i + 1)

        backtrack(s)

        return self.res

#WAY 2
class Solution:

    def solve(self,ip,op,l):
    	if len(op)==0:
    		l.add(ip)
    		return
    
    	self.solve(ip+op[0].upper(),op[1:],l)
    	self.solve(ip+op[0].lower(),op[1:],l)
    
    def letterCasePermutation(self, s: str) -> List[str]:
    	ip=''
    	op=s
    	l=set()
    	self.solve(ip,op,l)
    	return l