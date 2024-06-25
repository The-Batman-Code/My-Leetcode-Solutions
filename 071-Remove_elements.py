class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index


# Time : 33ms (81.49%) Space : 16.59 MB (49.03%)
