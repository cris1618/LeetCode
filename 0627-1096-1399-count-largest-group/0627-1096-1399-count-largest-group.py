class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash_map = Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hash_map[key] += 1
        max_val = max(hash_map.values())
        count = sum(1 for v in hash_map.values() if v == max_val)
        return count


        