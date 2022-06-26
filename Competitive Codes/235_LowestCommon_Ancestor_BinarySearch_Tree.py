#WAY 1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:  # Current is not empty
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:  # Anyone is equals to the curr i.e. the curr is the LCA
                return curr

#WAY 2

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      """
      time complexity: O(logN)
      space complexity: O(1)
      whenever cur_node.val is between p.val and q.val, it is LCA because we have a split
      when cur_node.val is greater than p.val and q.val, alghough it is a common ancestor,
      it is not the lowest. We should go to left subtree to find the lowest one.
      same logic when cur_node.val is lower than p.val and q.val, we need to go to right subtree
      """
      while True:
        if root.val < p.val and root.val < q.val:
          root = root.right
        elif root.val > p.val and root.val > q.val:
          root = root.left
        else:
          """
          either p or q is equal to root
          or root.val is between p.val and q.val (i.e. split occured)
          """
          return root