class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = dict(Counter(s)), dict(Counter(t))
        print(count_s, count_t)
        if count_s.keys() != count_t.keys():
            return False
        for e in count_s.keys():
            if count_s[e] != count_t[e]:
                return False
        return True


# Len should be same
# Count of each element should be same

# Time : 38ms (95.14%) Space : 17.09 MB (34.26%)
