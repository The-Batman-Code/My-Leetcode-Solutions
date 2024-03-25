# Approach -1
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, j, count, vowels = 0, k, 0, ["a", "e", "i", "o", "u"]

        def helperFunction(sub):
            count = 0
            for letter in sub:
                if letter in vowels:
                    count += 1
            return count

        while j <= len(s):
            count = max(count, helperFunction(s[i:j]))
            i += 1
            j += 1
        print(count)
        return count


# Approach -2
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        i = 1
        j = k
        m = 0
        vowels = set("aeiou")
        for letter in s[0:k]:
            if letter in vowels:
                count += 1
        m = count
        print(len(s))
        if k == len(s) - 1:
            return count
        print(count)
        while j <= len(s) - 1:
            print(count, s[j])
            if s[i - 1] in vowels:
                count -= 1
            if s[j] in vowels:
                count += 1
            m = max(m, count)
            i += 1
            j += 1
            # print(j, len(s))
            # print(count,s[i],s[i+1], s[j])
        return m


# Time : 569ms (6.12%) Space : 12.94 MB (86.03%)

#
