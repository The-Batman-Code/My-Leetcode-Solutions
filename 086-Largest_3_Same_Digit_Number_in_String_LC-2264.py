# Approach - 1
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dicta = defaultdict(int)
        for l in str(num):
            dicta[int(l)] += 1
        print(dicta)
        possible_ans = []
        for i, k in dicta.items():
            if k >= 3:
                possible_ans.append(i)

        ans = max(possible_ans)
        print(ans)
        return str(ans) * 3


# Approach - 2
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dicta = defaultdict(int)
        for l in str(num):
            dicta[int(l)] += 1
        print(dicta)
        possible_ans = []
        for i, k in dicta.items():
            if k >= 3:
                possible_ans.append(i)

        print(possible_ans)
        possible_ans.sort(reverse=True)
        for m in possible_ans:
            if str(m) * 3 in num:
                return str(m) * 3
        return ""


# Time : 41ms (43.01%) Space : 16.56 MB (50.42%)
