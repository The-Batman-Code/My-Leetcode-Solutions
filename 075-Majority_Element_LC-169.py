# Approach - 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        m = {}
        for i in nums:
            if i not in m.keys():
                m.update({i: 1})
            else:
                m[i] += 1
        print(m)
        for l, m in m.items():
            if m > n:
                return l
        return 5


# Time : 199ms (5.32%) Space : 18.10 MB (26.70%)


# Approach - 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res


# Time : 162ms (89.16%) Space : 17.91 MB (68.04%)
