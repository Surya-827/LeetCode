#Way 1 One Liner

class Solution(object):
    @classmethod
    def average(cls,salary : List[int]) -> float:
        return ((sum(salary) - min(salary) - max(salary))/(len(salary)-2))


#Way 2
class Solution(object):
    @classmethod
    def average(cls, salary: List[int]) -> float:
        s = sum(salary) - min(salary) - max(salary)
        l = len(salary)-2
        return s/l


