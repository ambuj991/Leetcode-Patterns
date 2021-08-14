# single nums
from collections import Counter

class Solution:
    def singleNumber(self,nums):
       
        c = Counter(nums)
        for key in c.elements():
            if c[key] == 1:
                return key
s = Solution()
print(s.singleNumber([1,1,2,2,3,3,4,5,5]))