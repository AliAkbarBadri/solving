# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy2(self, n: int) -> bool:
        slow, fast = n, self.square_digits(n)
        while slow != fast:
            slow = self.square_digits(slow)
            fast = self.square_digits(self.square_digits(fast))
        return fast == 1
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while True:
            n = self.square_digits(n)
            if n in seen_numbers:
                return False
            if n == 1:
                return True
            seen_numbers.add(n)
    def square_digits(self, n: int) -> int:
        result = 0
        while n != 0:
            result += (n%10)**2
            n //= 10
        return result
    def square_digits(self, n: int) -> int:
        result = 0
        for digit in str(n):
            result += int(digit) ** 2
        return result
    

sol = Solution()
assert sol.isHappy(1) == True
assert sol.isHappy(7) == True
assert sol.isHappy(19) == True
assert sol.isHappy(2) == False