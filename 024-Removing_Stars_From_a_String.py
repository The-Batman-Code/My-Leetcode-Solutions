class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        p = 0
        for e in s:
            if e != "*":
                stack.append(e)
            if e == "*":
                stack.pop()
        print(stack)
        return "".join(stack)


# Time : 462ms (24.78%) Space : 15.03 MB (28.17%)
