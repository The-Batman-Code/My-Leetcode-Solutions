# Approach -1
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # if only one or no element return -1
        if len(arr) == 1 or len(arr) == 0:
            return [-1]
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1 : len(arr)])

        arr[len(arr) - 1] = -1
        return arr


# Approach-2
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # if only one or no element return -1
        rm = -1
        for i in range(len(arr) - 1, -1, -1):
            nm = max(rm, arr[i])
            arr[i] = rm
            rm = nm
        return arr


# Time : 522ms (37.16%) Space : 18.12 MB (61.51%)
