from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        arr = [str(x) for x in arr]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        arr.sort(key=cmp_to_key(compare))

        if arr[0] == "0":
            return "0"

        return "".join(arr)


obj = Solution()
print(obj.findLargest([3, 30, 34, 5, 9]))