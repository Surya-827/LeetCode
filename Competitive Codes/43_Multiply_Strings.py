
class Solution(object):

    @classmethod
    def multiplyStrings(cls,n1:str,n2:str) -> str:
        return str(eval(f"{n1}*{n2}"))


if __name__=="__main__":

    obj = Solution()
    x = input()
    y = input()
    print(obj.multiplyStrings(x,y))
