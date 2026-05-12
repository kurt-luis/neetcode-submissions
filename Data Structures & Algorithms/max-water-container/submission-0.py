class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_vol = 0

        while i < j:
            while j > i:
                vol = (j - i) * min(heights[i], heights[j])

                if vol > max_vol:
                    max_vol = vol

                j -= 1
            i += 1
            j = len(heights) - 1

        return max_vol
