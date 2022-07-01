#WAY 1

class Solution(object):
    def isValid(self, k):
        if len(k) % 2 != 0: return False

        while len(k) != 0:
            if '()' in k:
                k = k.replace('()', '')
            elif '[]' in k:
                k = k.replace('[]', '')
            elif '{}' in k:
                k = k.replace('{}', '')
            else:
                return False

        if len(k) == 0: return True


#WAY 2

class Solution:
    '''
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
    if i in d: # 1
    stack.append(i)
    elif len(stack) == 0 or d[stack.pop()] != i: # 2
    return False
    return len(stack) == 0

    '''

    def isValid(self, s: str) -> bool:
        #storing matches
        dics = {
                "(" : ")",
                "[" : "]",
                "{" : "}"
            }
        stack = []
        for x in s:
            # if no element in stack, add it to there
            if len(stack) == 0:
                stack.append(x)
            else:
            #if there IS element, pop element to match
                pt = stack.pop()
                #check if pt is OPENING parentheses
                if pt in dics:
                    #if it match, move forward
                    if x == dics[pt]:
                        continue
                    else:
                    #append them back to stack
                        stack.append(pt)
                        stack.append(x)
                else:
                    return False
        #if after deletion there is still elements, then it is          not valid
        if len(stack) == 0:
            return True
        else:
            return False