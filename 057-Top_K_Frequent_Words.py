# Approach -1
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        unique_words = set(words)
        d = {}
        ans = []
        for l in words:
            if l not in d.keys():
                d.update({l: 1})
            else:
                d[l] += 1

        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        sorted_d = dict(sorted_d)
        keys = sorted_d.keys()
        for i in range(k):
            ans.append(list(sorted_d.keys())[i])
        print(ans)
        return ans


# Approach -2
class HeapItem:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __lt__(self, to_compare) -> bool:
        if self.count == to_compare.count:
            return self.word > to_compare.word
        return self.count < to_compare.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)

        heap = []
        for word, count in word_counts.items():
            item = HeapItem(word, count)

            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)

        res = []
        while k:
            cur = heapq.heappop(heap)
            res.append(cur.word)
            k -= 1
        res = reversed(res)
        return res


# Time : 58ms (58.07%) Space : 16.83 MB (9.20%)
