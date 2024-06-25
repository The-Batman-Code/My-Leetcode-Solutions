class MyHashSet:

    def __init__(self):
        self.l = []

    def add(self, key: int) -> None:
        if key not in self.l:
            self.l.append(key)

    def remove(self, key: int) -> None:
        if key in self.l:
            self.l.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.l:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Time : 725ms (19.94%) Space : 20.98 MB (96.13%)
