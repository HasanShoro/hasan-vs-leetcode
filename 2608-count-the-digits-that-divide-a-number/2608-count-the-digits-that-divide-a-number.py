class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        count = 0
        
        while num > 0:
            digit = num % 10      # gets the last digit
            num //= 10            # removes that digit
            
            if digit != 0 and original % digit == 0:
                count += 1
        
        return count
