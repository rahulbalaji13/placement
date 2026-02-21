class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = {2,3,5,7,11,13,17,19}
        return sum(bin(x).count('1') in primes for x in range(left, right + 1))
        
