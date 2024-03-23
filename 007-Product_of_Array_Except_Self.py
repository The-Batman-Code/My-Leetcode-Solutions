# Approach-1
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * (n + 1)
        output = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]

        prefix = [1] + prefix + [1]

        for l in range(n - 1, -1, -1):
            suffix[l] = nums[l] * suffix[l + 1]
        suffix = [1] + suffix
        print(prefix)
        print(suffix)

        for k in range(1, len(output) + 1):
            output[k - 1] = prefix[k - 1] * suffix[k + 1]

        return output


# Approach-2
# Time : 253ms (5.36%) Space : 21.76 MB (18.66%)
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        print(prefix)

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        print(suffix)

        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer
