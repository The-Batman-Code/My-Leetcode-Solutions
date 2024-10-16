# Approach - 1
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return -1
        if len(s) == 2 and s[0] == s[1]:
            return 0
        counts = collections.Counter(s)
        print(counts)
        more_than_one = []
        for i, j in counts.items():
            if j > 1:
                more_than_one.append(i)
        if more_than_one == []:
            return -1
        print(more_than_one)
        maxes = []
        for k in more_than_one:
            print(k)
            subs = [index for index, char in enumerate(s) if char == k]
            print(subs)
            for l in range(len(subs) - 1):
                maxes.append(max(subs) - min(subs) - 1)
                print(maxes)
        return max(maxes)


# Time : 65ms (6.49%) Space : 16.79 MB (30.80%)


# Approach - 2
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        res = -1

        for i, c in enumerate(s):
            if c in char_index:
                res = max(res, i - char_index[c] - 1)
            else:
                char_index[c] = i
        return res


# Time : 37ms (54.82%) Space : 16.55 MB (30.80%)
