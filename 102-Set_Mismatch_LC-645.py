# Approach - 1
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        ans = []
        for i, j in counts.items():
            if j > 1:
                ans.append(i)
        ans.append(ans[0] + 1)
        return ans


# Approch - 2
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        l = len(nums)
        ans = []
        for i, j in counts.items():
            if j > 1:
                ans.append(i)
        s = (l * (l + 1)) / 2
        k = sum(nums)
        ans.append(int(s - (k - ans[0])))
        return ans


# Time : 9ms (100.00%) Space : 17.94 MB (96.71%)
