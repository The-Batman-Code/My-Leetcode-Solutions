# Approach -1
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        unique = []
        for i in chars:
            if i in unique:
                continue
            else:
                unique.append(str(i))
        counts = []
        for i in unique:
            if chars.count(i) == 1:
                s += str(i)
            else:
                s += str(i)
                s += str(chars.count(i))
        for k in range(len(s)):
            chars[k] = s[k]

        for o in range(len(chars) - 1, len(s) - 1, -1):
            chars.pop(o)


# Approach -2
## Time : 45ms (5.84%) Space : 11.97 MB (49.69%)
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        index = 0
        n = len(chars)
        while i < n:
            curr_char = chars[i]
            count = 0
            while i < n and curr_char == chars[i]:
                i += 1
                count += 1
            print(count)

            chars[index] = curr_char
            index += 1
            if count > 1:
                for r in str(count):
                    chars[index] = r
                    index += 1

        print(chars)
        copy = chars[:]
        for i in range(len(copy), index, -1):
            chars.pop()
        return index
