class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1], [1, 1]]
        if numRows == 1:
            return [arr[0]]
        if numRows == 2:
            return arr

        def helper(arra):
            i, j = 0, 1
            temp = []
            for _ in range(len(arra)):
                while j < len(arra):
                    temp.append(arra[i] + arra[j])
                    i += 1
                    j += 1
            return temp

        temper = [1]
        for i in range(2, numRows):
            temper = temper + helper(arr[i - 1])
            temper.append(1)
            arr.append(temper)
            temper = [1]
        print(temper)
        print(arr)
        return arr


# Time : 28ms (94.99%) Space : 16.56 MB (57.63%)
