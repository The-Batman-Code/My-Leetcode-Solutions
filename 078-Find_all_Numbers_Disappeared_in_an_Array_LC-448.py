# Approach - 1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        test = [i for i in range(1, len(nums) + 1)]
        print(test)
        ans = []
        for i in test:
            if i not in nums:
                ans.append(i)
        return ans


# Time limit exceeded


# Approach - 2
class Solution:
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]


# Time : 250ms (75.74%) Space : 27.04 MB (42.67%)
