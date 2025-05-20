class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        # Build difference array from all query ranges
        for left, right in queries:
            diff[left] += 1
            if right + 1 < n:
                diff[right + 1] -= 1

        # Apply prefix sum to compute how many times each index is affected
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Check if each number can be decremented to 0
        for i in range(n):
            if nums[i] > diff[i]:
                return False

        return True