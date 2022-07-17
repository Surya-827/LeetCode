class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals.sort()
		stack = []
		# insert first interval into stack
		stack.append(intervals[0])
		for i in intervals[1:]:
			# Check for overlapping interval,
			# if interval overlap
			if stack[-1][0] <= i[0] <= stack[-1][-1]:
				stack[-1][-1] = max(stack[-1][-1], i[-1])
			else:
				stack.append(i)
		return stack