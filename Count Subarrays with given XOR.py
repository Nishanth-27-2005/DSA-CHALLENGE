class Solution:
    def countSubarraysWithXorK(self, arr, k):
        freq = {}
        prefix_xor = 0
        count = 0
        
        for num in arr:
            prefix_xor ^= num
            
            if prefix_xor == k:
                count += 1
            
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count


obj = Solution()
print(obj.countSubarraysWithXorK([4, 2, 2, 6, 4], 6))