import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=[i for i in range(1,n*2) if i%2==1]
        sumOdd=sum(odd)
        even=[i for i in range(1,n*2) if i%2==0]
        sumEven=sum(even)
        # while sumEven != 0:
        #     sumOdd,sumEven = sumEven, sumOdd%sumEven
        # return abs(sumOdd)
        return math.gcd(sumOdd,sumEven)