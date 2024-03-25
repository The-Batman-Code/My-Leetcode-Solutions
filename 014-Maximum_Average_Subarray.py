# Approach -1
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i, j = 0, k
        ans = float("-inf")
        while j <= len(nums):
            ans = max(ans, sum(nums[i:j]) / float(k))
            i += 1
            j += 1
        print(ans)

        return ans


# Approach-2
class Solution:
    def findMaxAverage(self, nums, k):

        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]

            maxSum = max(maxSum, currSum)
        return maxSum / float(k)


# Time : 910ms (71.52%) Space : 21.12 MB (50.50%)
