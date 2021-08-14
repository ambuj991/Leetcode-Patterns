# # top k frequent elements
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) == 1:
#             return [nums[0]]

# # freq dict
#         d = {}
#         for num in nums:
# 	        if num in d:
# 		        d[num] += 1
# 	        else:
# 		        d[num] = 1

# # insert k items into heap O(nlog(k))
#         h = []
#         from heapq import heappush, heappop
#         for key in d: # O(N)
# 	        heappush(h, (d[key], key)) # freq, item - O(log(k))
# 	        if len(h) > k:
# 		        heappop(h)

#         res = []
#         while h: # O(k)
# 	        frq, item = heappop(h) # O(logk)
# 	        res.append(item)
#         return res


# 2nd solutn which is O(n) is below  

def topKFrequent( nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        res= []
    
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))