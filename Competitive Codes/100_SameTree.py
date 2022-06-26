#WAY 1

class Solution:
	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		def traversal(node1,node2):
			if (node1 and node2):
				if (node1.val == node2.val and traversal(node1.left,node2.left) and traversal(node1.right,node2.right)):
					return True
				return False
			return node1 == node2

		return traversal(p,q)


# WAY 2

class Solution:
	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		def dfs(node_p, node_q):
			if node_p is None and node_q is None:
				return True

			if node_p is None or node_q is None or node_p.val != node_q.val:
				return False

			left = dfs(node_p.left, node_q.left)
			right = dfs(node_p.right, node_q.right)

			return left and right

		return dfs(p, q)
