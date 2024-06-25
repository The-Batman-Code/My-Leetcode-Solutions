class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        max1, max2, min1, min2 = nums[0], nums[1], nums[-1], nums[-2]
        return (max1 * max2) - (min1 * min2)


# Time : 154ms (6.08%) Space : 17.59 MB (99.57%)
