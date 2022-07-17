class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        non_overlapping = []
        count = 0

        for interval in intervals:
            if non_overlapping and non_overlapping[-1][1] > interval[0]:
                count += 1
            else:
                non_overlapping.append(interval)

        return count