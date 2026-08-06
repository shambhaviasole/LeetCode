class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            mul = 1

            for digit in str(n):
                mul *= int(digit)

            if mul % t == 0:
                return n

            n += 1