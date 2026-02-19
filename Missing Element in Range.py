class Solution:
    def missingRange(self, arr, low, high):
        #code here
        # ans = []
        # for i in range(low, high + 1):
        #     if i not in arr:
        #         ans.append(i)
        # return ans
        
        freq = {}
        for i in range(low, high+1):
            freq[i] = 1
        ans = []
        for i, j in freq.items():
            if i not in arr:
                ans.append(i)
        return ans
obj = Solution()