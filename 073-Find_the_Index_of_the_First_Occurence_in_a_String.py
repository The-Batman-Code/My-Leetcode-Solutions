# Approach -1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


# Approach -2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


# Time : 33ms (71.56%) Space : 16.43 MB (90.84%)
