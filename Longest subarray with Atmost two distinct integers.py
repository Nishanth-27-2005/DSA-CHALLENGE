class Solution:
    def totalElements(self, arr):
        left = 0
        freq = {}
        max_len = 0
        
        for right in range(len(arr)):
            # Expand window
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            
            # Shrink if more than 2 distinct
            while len(freq) > 2:
                freq[arr[left]] -= 1
                
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                
                left += 1
  
            max_len = max(max_len, right - left + 1)
        
        return max_len

arr = [7, 14, 17, 18, 5, 9, 20, 14, 19, 7, 16, 11, 7, 11, 10, 10, 15, 6, 14]
ob = Solution()
res = ob.totalElements(arr)

print(res)