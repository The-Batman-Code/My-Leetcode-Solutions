class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if not j in visited and isConnected[i][j] == 1:
                    dfs(j)

        n = len(isConnected)
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components


# Time : 177ms (51.30%) Space : 12.48 MB (40.37%)
