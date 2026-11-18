# 217. Contains Duplicate
# Approach: set, return as soon as a repeat is seen
# Time: O(n) | Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
