class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        table = {}
        for num in arr:
            if num not in table.keys():
                table.update({num: 0})
            if num in table.keys():
                table[num] += 1
        print(table)
        unique = set(table.values())
        for num in unique:
            if table.values().count(num) > 1:
                return False
        return True


# Time : 36ms (5.29%) Space : 11.88 MB (21.99%)
