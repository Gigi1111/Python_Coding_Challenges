# https://leetcode.com/problems/multiply-strings/solution/
## 
class Solution:
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    
    def strToInt(self, num: str) -> int:
        n = 0
        for i, val in enumerate(num): 
            index = self.nums.index(val)
            n += index*10**(len(num)-(i+1))
            
        return n
    
    def intToStr(self, num: int) -> str:
        if num == 0: return "0"
        num_str = ""
        i = 1
        while num > 0:
            remainder = num % 10**i
            num_str += str(remainder)[0]
            num -= remainder
            i += 1                
        return num_str[::-1]
            
    def multiply(self, num1: str, num2: str) -> str:
        # must not use any built-in BigInteger library or convert the inputs to integer directly.
        return self.intToStr(self.strToInt(num1) * self.strToInt(num2))
        