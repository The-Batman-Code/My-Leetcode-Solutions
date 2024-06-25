# Approach - 1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = [0] + nums1 + [0]
        nums2 = [0] + nums2 + [0]
        ans = []
        for i in range(1, len(nums1) - 1):
            ind = nums2.index(nums1[i])
            if nums2[ind + 1] > nums2[ind]:
                ans.append(nums2[ind + 1])
            else:
                ans.append(-1)
        print(ans)
        return ans


# Approach - 2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = [0] + nums1 + [0]
        nums2 = [0] + nums2 + [0]
        ans = []
        for i in range(1, len(nums1) - 1):
            ind = nums2.index(nums1[i])
            for j in range(ind, len(nums2) - 1):
                if nums2[j] > nums2[ind]:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        print(ans)
        return ans


# Approach - 3
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res


# Time : 40ms (93.51%) Space : 17.03 MB (9.02%)


# Approach - 4
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res


# Time : 47ms (67.51%) Space : 16.70 MB (96.33%)
