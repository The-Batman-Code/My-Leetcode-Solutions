# Time : 43ms (5.24%) Space : 12.30 MB (8.65%)
# Approach-1
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = [], []
        new_list = []
        si = list(s)
        si = [" "] + si + [" "]
        print(si)
        for i in range(0, len(si) - 1):
            if si[i] == " " and si[i + 1] != " ":
                start.append(i)
        print(start)

        for i in range(0, len(si) - 1):
            if si[i] != " " and si[i + 1] == " ":
                end.append(i)
        print(end)

        for l in range(len(start)):

            new_list.append("".join(si[start[l] + 1 : end[l] + 1]))
        new_list.reverse()
        return " ".join(new_list)


# Approach -2


class Solution(object):
    # Time : 18ms (45.11%) Space : 12.18 MB (8.65%)
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_list = s.split()
        new_list.reverse()
        return " ".join(new_list)
