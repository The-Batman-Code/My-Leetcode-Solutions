class Solution:
    def nCr(self, n, r):
        return self.fact(n) / (self.fact(r) * self.fact(n - r))

    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        res = 1

        for i in range(2, n + 1):
            res = res * i

        return res

    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        for key, value in counts.items():
            if value > 1:
                ans += self.nCr(value, 2)
                print(ans)
        print(counts)
        return int(ans)


# Time : 33ms (79.70%) Space : 16.67 MB (7.05%)
