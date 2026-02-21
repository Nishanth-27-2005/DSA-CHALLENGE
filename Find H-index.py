class Solution:
    def hIndex(self, citations):
        length = len(citations)
        arr = [0] * (length + 1)

        for i in range(length):
            if citations[i] > length:
                arr[length] += 1
            else:
                arr[citations[i]] += 1

        total = 0
        for i in range(length, -1, -1):
            total += arr[i]
            if total >= i:
                return i

        return 0


# simple test
obj = Solution()
print(obj.hIndex([3, 0, 6, 1, 5]))