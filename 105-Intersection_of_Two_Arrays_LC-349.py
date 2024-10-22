# Approach - 1
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = nums1.copy()
        for i in nums2:
            l.append(i)

        l = set(l)
        ans = []
        for i in l:
            if i in nums2 and i in nums1:
                ans.append(i)
        print(ans)
        return ans


# Approach - 2
class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        result = []

        for num in set2:
            if num in set1:
                result.append(num)

        return result


# Time : 3ms (97.80%) Space : 16.73 MB (37.61%)
