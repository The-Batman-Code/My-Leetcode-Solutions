class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        while len(nums) > 0:
            n = nums.pop(0)
            count[n] += 1
            print(nums)
        print("------------")
        print(count)
        for i in range(len(count)):
            for l in range(count[i]):
                nums.append(i)

        print(nums)


# Time : 25ms (98.88%) Space : 16.58 MB (19.58%)
