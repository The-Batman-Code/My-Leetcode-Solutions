# Approach -1
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        def helperFunction():
            i, j = 0, 1
            for _ in range(len(nums)):
                if j >= len(nums):
                    return False
                print(nums[i], nums[j])
                if nums[i] + nums[j] == k:
                    nums.pop(j)
                    nums.pop(i)
                    return True
                j += 1
            return False

        for _ in range(len(nums)):
            if helperFunction():
                count += 1

        return count


# Approach -2
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, l, r = 0, 0, len(nums) - 1
        nums.sort()

        while l < r:
            if (nums[l] + nums[r]) < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
                r -= 1
                ans += 1


# Time : 532ms (28.60%) Space : 21.40 MB (55.81%)
