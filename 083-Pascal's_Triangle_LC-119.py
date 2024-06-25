# Approach - 1
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        arr = [1, 1]

        for i in range(1, rowIndex):
            arr = [1] + [arr[j] + arr[j + 1] for j in range(len(arr) - 1)] + [1]
            print(arr)
        return arr


# Time : 36ms (50.46%) Space : 16.32 MB (94.71%)
