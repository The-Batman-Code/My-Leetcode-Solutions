class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()

        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)

        dfs(0)
        return len(visited) == len(rooms)


# Time : 39ms (74.30%) Space : 12.47 MB (23.38%)
