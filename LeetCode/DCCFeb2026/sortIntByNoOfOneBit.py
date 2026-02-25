class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort(key = lambda num: (bin(num).count("1"), num))
        return arr
