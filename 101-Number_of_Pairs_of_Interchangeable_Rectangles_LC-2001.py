# Approach - 1
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = Counter([i[0] / i[1] for i in rectangles])
        greater = []
        for i, j in counts.items():
            if j > 1:
                greater.append(j)
        ans = 0
        for m in greater:
            ans += (m * (m - 1)) / 2
            print(ans)
        return int(ans)


# Time : 1283ms (95.79%) Space : 73.53 MB (11.96%)
