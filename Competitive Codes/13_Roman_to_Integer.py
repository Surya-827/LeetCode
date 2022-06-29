class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        value = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        # example s = "MCMXCIV"

        s = s[::-1]  # reverse string i.e s = "VICXMCM"

        total = value[s[0]]  # set total to value[s[0]] in reversed string i.e 'V'

        for i in range(1, len(s)):  # for all the letters except first i.e value[s[0]]

            # subtract if the value[s[i]](value[s[1]]) i.e "I"
            # is less than value[s[i-1]](value[s[0]]) i.e "V"
            if value[s[i]] < value[s[i - 1]]:
                total -= value[s[i]]

            # else add the value
            else:
                total += value[s[i]]
        return total