class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        

        for i in range(n):
            cnt = defaultdict(int)

            for j in range(i, n):
                cnt[s[j]] += 1
                
                balence_set = set(cnt.values())
                cnt_len = len(balence_set)

                if cnt_len == 1:
                    res = max(res, j - i + 1)

        return res

# Time complexity = O(C X K^2)
        
