class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        l = [0]
        for i in range(len(gain)):
            l.append(l[i] + gain[i])
        print(l)
        return max(l)


# Time : 21ms (24.44%) Space : 11.71 MB (11.15%)
