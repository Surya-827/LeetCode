class Solution (object):
  def groupAnagrams(self,s:List[str]) -> List[List[str]]:
    d = dict()
    for i in s:
      t = ''.join(sorted(i))
      if t in d:
        d[t].append(i)
      else:
        d[t]=[i]
    res=[]
    ans = sorted(res,key=lambda x: len(x))
    return ans
  
  
  if __name__=="__main__":
    obj = Solution()
    s = list(map(str,input().split()))
    print(obj.groupAnagrams(s))
