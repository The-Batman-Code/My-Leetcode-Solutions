# Approach -1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(set(s)) == len(set(t)):
            return True
        else:
            return False


# Approach -2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapST, mapTS = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True


# Time : 43ms (50.60%) Space : 16.72 MB (59.81%)
