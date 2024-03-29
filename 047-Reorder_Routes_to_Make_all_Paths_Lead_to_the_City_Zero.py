class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        edges = {(a, b) for a, b in connections}
        neighbours = {city: [] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):  # Indent the function definition here
            nonlocal edges, neighbours, visit, changes

            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue
                if (neighbour, city) not in edges:
                    changes += 1
                visit.add(neighbour)
                dfs(neighbour)

        visit.add(0)
        dfs(0)

        print(neighbours)
        print(edges)
        return changes


# Time : 1052ms (9.97%) Space : 53.08 MB (16.19%)
