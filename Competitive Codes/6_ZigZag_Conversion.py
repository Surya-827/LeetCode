class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]

        for i, c in enumerate(s):
            remainder = i % (numRows * 2 - 2)
            if remainder < numRows:
                rows[remainder].append(c)
            else:
                rows[numRows - 1 - (remainder - numRows + 1)].append(c)

        return ''.join([''.join(row) for row in rows])


if __name__=="__main__":

    obj = Solution()
    s = "PAYPALISHIRING"#input()
    numRows = 4#int(input())
    print(obj.convert(s,numRows))