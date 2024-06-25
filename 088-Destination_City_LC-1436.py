class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for p in paths:
            s.add(p[0])

        for p in paths:
            if p[1] not in s:
                return p[1]


# Time : 62ms (23.03%) Space : 16.44 MB (95.36%)
