# Time : 25ms (19.22%) Space : 11.65 MB (42.69%)
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_value = max(candies)
        temp = [(i + extraCandies) for i in candies]
        return [True if l >= max_value else False for l in temp]
