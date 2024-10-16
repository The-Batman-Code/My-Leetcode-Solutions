# Approach - 1
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        for i in words:
            for k in i:
                if k in d:
                    d[k] += 1
                else:
                    d.update({k: 1})
        for m in d.values():
            if m % len(words) != 0:
                return False
        return True


# Time : 61ms (55.00%) Space : 16.82 MB (8.41%)
