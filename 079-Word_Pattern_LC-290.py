# Approach - 1
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = []
        temp = []
        words = s.split(" ")
        ans1 = set(words)
        ans2 = set(pattern)
        print(ans1, ans2)
        return len(ans1) == len(ans2)


# Approach - 2
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        l = s.split(" ")

        if len(l) != len(pattern):
            return False

        d = {}
        se = set()

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] not in se:
                    d[pattern[i]] = l[i]
                    se.add(l[i])
                else:
                    return False

        return True


# Time : 30ms (84.48%) Space : 16.50 MB (48.47%)
