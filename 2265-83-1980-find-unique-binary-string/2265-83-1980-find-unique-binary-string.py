from itertools import product
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        all_binaries = {"".join(p) for p in product("01", repeat=n)}

        for binary in all_binaries:
            if binary not in nums:
                return binary
        