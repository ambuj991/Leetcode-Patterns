import collections

def majorityElement(nums):
        counts = collections.Counter(nums)
        print(counts)
        return max(counts.keys(), key=counts.get)

3

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         d = {}
#         for i in nums:
#             if i not in d:
#                 d[i] =1
#             else:
#                 d[i]+=1
#         n = len(nums)//2
#         for i in d:
#             if d[i] > n:
#                 return i

print( majorityElement( [2,2,1,1,1,2,2]))