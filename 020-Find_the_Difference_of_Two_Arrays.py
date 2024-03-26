class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        inner_list = []
        outer_list = []
        seen = []
        for j in nums1:
            if j not in nums2 and j not in seen:
                inner_list.append(j)
                seen.append(j)
        outer_list.append(inner_list)
        inner_list = []
        seen = []
        for k in nums2:
            if k not in nums1 and k not in seen:
                inner_list.append(k)
                seen.append(k)
        outer_list.append(inner_list)
        print(outer_list)
        return outer_list


# Time : 547ms (5.04%) Space : 11.88 MB (95.46%)
