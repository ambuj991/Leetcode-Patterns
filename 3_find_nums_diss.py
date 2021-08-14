# find numers disappeared

class Solution:
    def findDisappearedNumbers( nums):
        l=len(nums)
        nums=set(nums)
        a=[]
        for i in range(1,l+1):
            if i not in nums:
                a.append(i)
        return a
        