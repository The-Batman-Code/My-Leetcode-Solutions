class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(1) == len(nums):
            return len(nums) - 1
        if nums.count(0) == len(nums):
            return 0
        i, j, zeroes, count = 0, 0, 0, 0
        while j < len(nums):
            if nums[j] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[i] == 0:
                    zeroes -= 1

                i += 1
            count = max(count, j - i)
            j += 1

        return count


# Time : 428ms (93.71%) Space : 14.70 MB (89.77%)
