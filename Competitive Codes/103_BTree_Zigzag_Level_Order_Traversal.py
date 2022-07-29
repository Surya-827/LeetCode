class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = collections.deque()
        res = []

        if not root:
            return res

        LTR = False

        queue.append(root)

        while queue:

            queue_len = len(queue)
            curr_level = collections.deque()

            for _ in range(queue_len):

                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

                if LTR:
                    curr_level.appendleft(curr_node.val)
                else:
                    curr_level.append(curr_node.val)

            LTR = not LTR
            res.append(list(curr_level))

        return res