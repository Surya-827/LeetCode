
# WAY 1 ONE LINER
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         return (high-low+1)//2 + (low%2+high%2)//2


# WAY 2
class Solution(object):
    def countOddNumbers(self,start:int,end:int) -> int:
        count=0
        for i in range(start,end+1):
            x = lambda x: 0 if x%2==0 else 1
            if(x(i)==1):
                count+=1
            else:
                continue
        return count

if __name__=="__main__":

    obj = Solution()
    x,y = map(int,input().split(" "))
    print(obj.countOddNumbers(x,y))