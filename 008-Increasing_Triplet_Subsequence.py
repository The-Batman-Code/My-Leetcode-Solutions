# Time : 815ms (89.38%) Space : 26.34 MB (34.26%)
class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
