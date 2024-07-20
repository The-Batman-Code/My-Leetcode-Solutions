# Approach - 1 Brute Force
class Solution:
    def maxScore(self, s: str) -> int:
        ans = []
        for i in range(1, len(s)):
            l = s[:i]
            c = s[:i].count("0")
            r = s[i:]
            m = s[i:].count("1")
            print("Left", l, "Right", r, "count_l", c, "count_r", m)
            ans.append(c + m)

        return max(ans)


# Approach - 2
class Solution:
    def maxScore(self, s: str) -> int:
        z = 0
        o = s.count("1")
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                z += 1
            else:
                o -= 1
            res = max(res, o + z)
        return res


# Time : 31ms (74.47%) Space : 16.43 MB (76.28%)
