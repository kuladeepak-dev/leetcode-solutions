# Two pointer approach
# time - O(n): each step moves one pointer, at most n - 1 steps
# space - O(1): only a few variables

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, h * width)

            # short wall caps height and moving inward shrinks width,
            # so it can't beat the current area: discard it
            if height[left] < height[right]:
                left += 1
            # right wall is shorter or equal: move right
            else:
                right -= 1

        return max_area
