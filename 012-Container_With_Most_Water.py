# Time : 535ms (42.16%) Space : 22.02 MB (86.52%)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
