class Solution:
	def intToRoman(self, num: int) -> str:
		rome = { 1: 'I', 5: 'V', 4: 'IV', 10: 'X', 9: 'IX', 50: 'L', 40: 'XL', 100: 'C', 90: 'XC', 500: 'D', 400: 'CD', 1000: 'M', 900: 'CM' }

		R = ''
		for i in range(3,-1,-1):
			conv = num//(10**i)
			if 0 < conv < 4:
				for k in range(conv):
					R += rome[10**i]
			elif 5 < conv < 9:
				R+= rome[5*(10**i)]
				for k in range(conv-5):
					R += rome[10**i]
			elif conv in  [9, 5, 4] :
				R += rome[conv*(10**i)]
			num -= conv*(10**i)
		return R