# Approach - 1
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        m = set()
        l = len(s) - 1
        while l != 0:
            if s[0] == s[l]:
                for i in range(1, len(s[0 + 1 : l]) + 1):
                    st = s[0] + s[i] + s[l]
                    print(st)
                    if st not in m:
                        print(st)
                        m.add(st)
                        count += 1

            l -= 1
            print(count)
        return 5


# Approach - 2
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])

            for j in range(26):
                c = chr(ord("a") + j)
                if c in left and c in right:
                    res.add((s[i], c))
            left.add(s[i])

        return len(res)


# Time : 2499ms (9.73%) Space : 17.56 MB (23.92%)
