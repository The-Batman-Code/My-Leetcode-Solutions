class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = []
        cols = []
        count = 0
        for i in range(len(grid)):
            for e in range(len(grid[i])):
                row.append(grid[e][i])
            cols.append(row)
            row = []
        print(cols)
        for e in grid:
            if e in cols:
                print(e)
                count += cols.count(e)
                print(cols.count(e))
        return count


# Time : 730ms (15.25%) Space : 15.96 MB (85.93%)
