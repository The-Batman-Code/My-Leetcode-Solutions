# Approach - 1
class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        if len(s) % 2:
            if s[0] == "1":
                sums = len(s) - len(s) // 2
                ans = abs(sums - s.count("1"))
                print(ans)
            else:
                sums = (len(s) - 1) / 2
                ans = abs(sums - s.count("1"))
                print(ans)
        else:
            ans = abs(len(s) / 2 - s.count("1"))
        return int(ans)


# Approach - 2
class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            if i % 2:
                count += 1 if s[i] == "0" else 0
            else:
                count += 1 if s[i] == "1" else 0

        return min(count, len(s) - count)


# Time : 49ms (42.73%) Space : 16.69 MB (63.00%)
