# def minMeetingRooms(self, intervals):
      
#         start = sorted([i.start for i in intervals])
#         end = sorted([i.end for i in intervals])
#         s, e = 0, 0
#         res, count = 0, 0

#         while s < len(intervals):
#             if start[s] < end[e]:
#                 s=s+1
#                 count=count+1
#             else:
#                 count -= 1
#                 e=e+1
#             res = max(res, count)
#         return res


import heapq

def minMeetingRooms( intervals):

        size = len(intervals)
        if size<=1: return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0]>=heap[0]:
                heapq.heappushpop(heap,interval[1])
            else:
                heapq.heappush(heap,interval[1])
        
        return len(heap)

a = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRooms( a))

# Time Complexity: O(N log N).
# There are two major portions that take up time here. One is sorting of 
# the array that takes O(N log N) considering that the array consists of N elements.
# Then we have the min-heap. In the worst case, all N meetings will collide with each other. 
# In any case we have N add operations on the heap. 
# In the worst case we will have N extract-min operations as well.
#  Overall complexity being (N log N) since extract-min operation on a heap takes O(log N).