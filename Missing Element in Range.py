class Solution:
    def missingRange(self, arr, low, high):
        #code here
        # ans = []
        # for i in range(low, high + 1):
        #     if i not in arr:
        #         ans.append(i)
        # return ans
        
        arr_set = set(arr)
        ans = []
        for i in range(low, high + 1):
            if i not in arr_set:
                ans.append(i)
        return ans

obj = Solution()