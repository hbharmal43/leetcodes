class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)- 1
        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif (nums[m]>target):
                r = m-1
            else:
                return m
        return -1

# Learning Curve: If you want to divinde integer and get integer in python, you can use // operator. It will give you integer value.