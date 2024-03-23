# Time : 160ms (26.21%) Space : 16.32 MB (21.11%)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "A", "E", "I", "O", "U", "e", "i", "o", "u"]
        stg = list(s)
        l = []
        for i in s:
            if i in vowels:
                l.append(i)
        l.reverse()
        print(l)
        for k in range(len(stg)):
            if stg[k] in vowels:
                stg[k] = l[0]
                l.pop(0)

        return "".join(stg)
