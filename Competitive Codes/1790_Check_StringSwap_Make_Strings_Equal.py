
class Solution(object):
    def areAlmostEqual(self,s1:str,s2:str) -> bool:
        points = []
        for i in range(len(s1)):
            if len(points)==3:
                break
            if(s1[i]!=s2[i]):
                points.append(i)
        if(points==[] or (len(points)==2 and s1[points[0]]==s2[points[1]] and s1[points[1]]==s2[points[0]])):
            return True
        return False



if __name__=="__main__":
    obj = Solution()
    s1 = input()
    s2 = input()
    print(obj.areAlmostEqual(s1,s2))
