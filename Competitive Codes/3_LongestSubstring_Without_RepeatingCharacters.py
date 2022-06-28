
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we define a start pointer for the start index of current candidate substring
        start = 0
        max_length = 0
        # we create a dictionary to record every char we've seen and its index
        record = dict()

        # to find the longest substring, we have to go through every char in s
        for i, char in enumerate(s):
            # if char in record, it means we have seen this char before, so we have to move the start pointer one step ,
            # forward from the previous identical char #edge case: pwwkew
            # note that start are not allowed to move backwards, so we have to check the where would start update to if,
            # we want to change it. edgecase: abba
            # another way to think about this is: start is the begining index of the substring, so if we see a duplicate,
            # char but it is on the left side of start, it does not affect the current substring, so we just update the ,
            # index of the duplicate char as if it is first seen. Otherwise, if the index of this duplicate char is on ,
            # the right side of start, it is really a duplicate char so we have to move the start.
            # so this if condition is saying: we see the current char, and we have the same char in the record, and its,
            # original index in on the right of char, that is, this char is already in the substring started from the ,
            # start index, then we have to move the start index to the next index of the original duplicate char,
            # then we also update the position of this char.
            if char in record and start <= record[char]:
                start = record[char] + 1
            record[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length

if __name__=="__main__":

    obj = Solution()
    s = input()
    print(obj.lengthOfLongestSubstring(s))


