# https://leetcode.com/problems/jump-game-ii/ 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        # to speed things up, pow two at a time
        if n % 2 == 0:
            ans = self.myPow(x*x, abs(n)/2)
        else:
            ans = x * self.myPow(x, abs(n)-1)

        return ans if n>0 else 1/ans

