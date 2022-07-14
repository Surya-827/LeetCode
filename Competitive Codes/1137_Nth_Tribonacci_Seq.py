
#WAY 1
def tribonacci(self, n: int) -> int:
    t0, t1, t2 = 0, 1, 1
    for _ in range(n-2):
        temp1 = t0
        temp2 = t1
        t0 = t1
        t1 = t2
        t2 = t2 + temp2 + temp1

    if n!=0:
        return t2
    else:
        return 0


#WAY 2
class Solution(object):
    @classmethod
    def tribonacci(cls,n:int) -> int:
        x,y,z = 0,1,1

        for _ in range(n-2):
            t1 = x
            t2 = y
            x = y
            y = z
            z = y + t1 + t2

        return z n!=0 else 0



if __name__=="__main__":
    obj = Solution()
    n = int(input())

    print(obj.tribonacci(n))