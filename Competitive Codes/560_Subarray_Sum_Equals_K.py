#WAY 1

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		ans=0
		prefsum=0
		d={0:1}

		for num in nums:
			prefsum = prefsum + num

			if prefsum-k in d:
				ans = ans + d[prefsum-k]

			if prefsum not in d:
				d[prefsum] = 1
			else:
				d[prefsum] = d[prefsum]+1

		return ans


#WAY 2
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		# negative values: can't use sliding window!

		count = defaultdict(int)
		count[0] = 1  # implicitly 0 index has prefix of 0
		currentPrefixSum = 0
		res = 0

		for num in nums:
			currentPrefixSum += num
			toFind = currentPrefixSum - k
			res += count[toFind]
			count[currentPrefixSum] += 1
		return res