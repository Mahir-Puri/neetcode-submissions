
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}

        # Build the complete graph first
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            # Cycle detected
            if crs in visitSet:
                return False

            # No prerequisites left
            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)

            # Course has been fully checked
            preMap[crs] = []

            return True

        # Check all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
