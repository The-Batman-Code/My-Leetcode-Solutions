# Approach-1
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == nums.count(0):
            return
        if len(nums) == nums.count(1):
            return
        start = 0
        global end
        end = len(nums) - 1

        def helperFunction(start):
            global end
            if start == end:
                return
            for i in range(start, end):
                nums[i] = nums[i + 1]
            nums[end] = 0
            print(nums)
            end -= 1

        for _ in range(len(nums)):
            while nums[start] == 0:
                helperFunction(start)
            start += 1
            if start == end:
                return


# Approach-2
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


# Time : 121ms (45.94%) Space : 13.67 MB (12.11%)
