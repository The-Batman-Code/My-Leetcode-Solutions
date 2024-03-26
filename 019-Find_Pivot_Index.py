# Approach -1
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fore_sum = []
        last_sum = []
        total = sum(nums)
        temp = 0
        for i in range(len(nums)):
            fore_sum.append(total - nums[i])
            total = total - nums[i]
        for j in range(len(nums) - 1, -1, -1):
            last_sum.append(temp + nums[j])
            temp = temp + nums[j]

        print(fore_sum)
        print(last_sum)
        return 5


# Approach -2
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum, right_sum = 0, sum(nums)
        nums = [0] + nums + [0]
        for i in range(1, len(nums)):
            left_sum = left_sum + nums[i - 1]
            print(nums[i])
            right_sum = right_sum - nums[i]
            if left_sum == right_sum:
                return i - 1
        return -1


# Approach -3
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)

        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


# Time : 95ms (96.34%) Space : 12.70 MB (91.99%)
