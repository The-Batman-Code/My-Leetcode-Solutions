# Approach -1
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ranger = 2 * len(nums)
        count = 0
        print(ranger)
        for i in range(ranger):
            if i > len(nums) - 1:
                print(len(nums) - i)
                ans.append(nums[count])
                count += 1
            else:
                ans.append(nums[i])

        return ans


# Time : 74ms (31.11%) Space : 17.13 MB (20.29%)


# Approach -2
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


# Time : 29ms (80.97%) Space : 16.89 MB (73.36%)
