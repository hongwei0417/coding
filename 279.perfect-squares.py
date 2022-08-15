#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        queue = [(0, 0)]
        visited = set([0])
        
        while queue:
            (curr_sum, count) = queue.pop(0)
            i = 0
            while True:
                i += 1
                new_sum = curr_sum + i * i
                if new_sum == n:
                    return count+1
                elif new_sum > n:
                    break
                elif new_sum in visited:
                    continue
                queue.append((new_sum, count+1))
                visited.add(new_sum)
# @lc code=end

s = Solution()
s.numSquares(12)

