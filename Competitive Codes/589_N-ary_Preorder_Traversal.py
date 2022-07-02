#  WAY 1 Recursive using DFS:

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node):
            if not node: return
            ans.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return ans
# WAY 2 Iterative:

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return
#         lst, res = [root], []
#         while lst:
#             child = lst.pop(0)
#             res.append(child.val)
#             lst = child.children + lst
#         return res