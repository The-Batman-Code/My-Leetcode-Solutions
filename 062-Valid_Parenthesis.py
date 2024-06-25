class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i in "{([":
                stack.append(i)
            else:
                if not stack:
                    return False
                l = stack.pop()
                comb = l + i
                if comb != "[]" and comb != "{}" and comb != "()":
                    return False
        return not stack


# Time : 29ms (90.45%) Space : 16.60 MB (75.34%)
