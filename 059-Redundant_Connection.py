# Approach -1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {c: [] for c in range(1, len(edges) + 1)}
        ans = 0
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        visit, cycle = set(), set()

        def dfs(data):
            if data in cycle:
                return data
            if data in visit:
                return data
            cycle.add(data)
            for e in graph[data]:
                ans = dfs(e)
            cycle.remove(data)
            visit.add(data)

        for i in range(1, len(edges) + 1):
            ans = dfs(i)
            print(ans)


# Approach-2
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbours = defaultdict(list)

        def dfs(x, y):
            if x == y:
                return True

            for n in neighbours[x]:
                if n not in visited:
                    visited.add(n)
                    if dfs(n, y):
                        return True
            return False

        for x, y in edges:
            visited = set()
            if dfs(x, y):
                return [x, y]
            neighbours[x].append(y)
            neighbours[y].append(x)


# Time : 67ms (12.36%) Space : 17.48 MB (16.27%)
