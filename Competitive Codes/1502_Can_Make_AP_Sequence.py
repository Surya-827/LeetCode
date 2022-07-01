class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        dif = []
        for i in range(len(arr)-1):
            dif.append(abs(arr[i]-arr[i+1]))
            if(dif[0]!=dif[i]):
                return False
        return True