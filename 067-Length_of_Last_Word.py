# Approach -1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()
        return len(ans[-1])


# Time : 43ms (6.46%) Space : 16.57 MB (81.87%)


# Approach-2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


# Time : 28ms (91.27%) Space : 16.56 MB (81.87%)
