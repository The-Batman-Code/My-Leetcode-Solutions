class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False


# Time : 442ms (16.94%) Space : 32.11 MB (24.62%)
