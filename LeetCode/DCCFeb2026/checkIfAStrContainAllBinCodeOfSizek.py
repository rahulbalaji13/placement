class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        seen = set()
        
        for i in range(len(s) - k + 1): #Sliding window
            seen.add(s[i:i+k])

        return len(seen) == 2 ** k
        
