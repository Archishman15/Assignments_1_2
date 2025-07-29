class Solution:
    def largest(self, arr):
        if not arr:
            return -1 

        max_val = arr[0]
        for num in arr[1:]:
            if num > max_val:
                max_val = num
        return max_val
