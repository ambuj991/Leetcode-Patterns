# find k pairs with smallest sums
import heapq
def kSmallestPairs(nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
     
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
print(kSmallestPairs( nums1 = [1,7,11], nums2 = [2,4,6], k = 3 ))

#  O(klgm) time and O(m) space