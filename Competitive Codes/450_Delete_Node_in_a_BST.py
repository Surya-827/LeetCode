class Solution(object):
	def deleteNode(self, root, key):
		if not root:
			return root
		if root.val==key:
			return self.helper(root)
		dummy = root
		while root:
			if root.val>key:
				if root.left and root.left.val == key:
					root.left = self.helper(root.left)
					break
				else:
					root=root.left
			else:
				if root.right and root.right.val == key:
					root.right = self.helper(root.right)
					break
				else:
					root=root.right
		return dummy
	def helper(self,root):
		if not root.left:
			return root.right
		elif not root.right:
			return root.left
		rightChild = root.right
		lastRight = self.findLastRight(root.left)
		lastRight.right = rightChild
		return root.left
	def findLastRight(self,root):
		if not root.right:
			return root
		return self.findLastRight(root.right)