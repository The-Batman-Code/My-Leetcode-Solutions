# Approach - 1
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        for i in range(1, N):
            preRow1[i] += preRow1[i - 1]
            preRow2[i] += preRow2[i - 1]

        print(preRow1)
        print(preRow2)

        res = float("inf")
        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i - 1] if i > 0 else 0
            sr = max(top, bottom)
            res = min(res, sr)
        return res


# Time : 187ms (94.45%) Space : 31.34 MB (97.45%)
