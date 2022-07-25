class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 0:
            return []
        inDegree = {}
        adjList = {}

        for i in range(numCourses):
            inDegree[i] = 0
            adjList[i] = []

        for child, parent in prerequisites:
            adjList[parent].append(child)
            inDegree[child] += 1

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        order = []
        visit = set()
        while len(q) > 0:
            cur = q.popleft()
            order.append(cur)
            visit.add(cur)

            for n in adjList[cur]:
                inDegree[n] -= 1
                if n not in visit and inDegree[n] == 0:
                    q.append(n)

        if len(order) == numCourses:
            return order
        return []