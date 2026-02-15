class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""

        while i >= 0 or j >=0 or carry:
            total = carry

            if i >= 0:
                total+=int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            res = str(total % 2) + res  # Add remainder
            carry = total // 2                 # Update carry

        return res


        
