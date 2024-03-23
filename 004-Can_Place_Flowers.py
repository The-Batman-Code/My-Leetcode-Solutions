# Approach-1
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        max_value = (len(flowerbed) // 2) + 1
        count_ones = flowerbed.count(1)
        if count_ones + n == max_value:
            return True
        return False


# Approach-2
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        print(flowerbed[0:2])
        print(flowerbed[len(flowerbed) - 2 : len(flowerbed)])

        if flowerbed[0:2] == [0, 0]:
            count += 1
        elif flowerbed[len(flowerbed) - 2 : len(flowerbed)] == [0, 0]:
            count += 1

        for i in range(1, (len(flowerbed) // 2) + 1):
            if flowerbed[i : i + 3] == [0, 0, 0]:
                count += 1
        count_ones = flowerbed.count(1)
        max_flowers = count_ones + count
        print(count_ones, max_flowers)
        return count_ones + n <= max_flowers


# Approach-3
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbeds = [0] + flowerbed + [0]

        for i in range(1, len(flowerbeds) - 1):
            if flowerbeds[i - 1] == 0 and flowerbeds[i] == 0 and flowerbeds[i + 1] == 0:
                flowerbeds[i] = 1

        flower_count = flowerbeds.count(1)
        return flowerbed.count(1) + n <= flower_count


# Time : 107ms (96.25%) Space : 12.52 MB (18.16%)
