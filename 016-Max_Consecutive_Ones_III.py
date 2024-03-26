# Approach -1
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j, count, ans = 0, 0, []
        for i in range(len(nums)):
            while i <= j and j < len(nums):
                if count == k:
                    break
                if nums[j] == 0:
                    count += 1
                j += 1
            while j < len(nums) and nums[j] == 1:
                j += 1
            ans.append(j - i)
            j = i + 1
            count = 0
        print(ans)

        return max(ans)


# Approach -2
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        zeroes = 0
        maxv = 0

        while end < len(nums):
            if nums[end] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[start] == 0:
                    zeroes -= 1

                start += 1
            maxv = max(maxv, end - start + 1)
            end += 1

        return maxv


# Time : 449ms (47.13%) Space : 12.02 MB (75.30%)
