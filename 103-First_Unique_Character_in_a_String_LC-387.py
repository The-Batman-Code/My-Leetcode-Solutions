# Approach - 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1


# Approach - 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        print(c)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1


# Time : 55ms (98.11%) Space : 16.78 MB (99.76%)
