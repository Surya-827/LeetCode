class Solution:
	def getMaxLen(self, nums: List[int]) -> int:
		start=last_neg=-1
		neg=res=0
		for i,x in enumerate(nums):
			if x==0:
				start=last_neg=i
				neg=0
			elif x<0:
				if neg==0:
					last_neg=i
				neg+=1
			res=max(res,(i-last_neg) if neg%2 else (i-start))
		return res