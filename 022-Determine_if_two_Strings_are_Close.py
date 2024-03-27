from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)

        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])

        print(n1)
        print(n2)
        print(c1 == c2)
        print(c1)
        print(c2)
        return c1 == c2 or (n1 == n2 and set(word1) == set(word2))


# Time : 381ms (17.63%) Space : 13.66 MB (31.01%)
