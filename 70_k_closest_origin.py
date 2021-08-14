import heapq
def kClosest(points, k):
        minHeap = []
        res = []
        for x,y in points:
            d = (x**2 + y**2)      
            minHeap.append([d, x,y])
        heapq.heapify(minHeap)
        
        while k:
            k=k-1
            d, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res

# O(klogn)