# sort characters by frequency
import collections
import heapq
def frequencySort(self, s: str) -> str:
	# Count the occurence on each character
	cnt = collections.Counter(s)
	
	# Build string
	res = []
	for k, v in cnt.most_common():
		res += [k] * v
	return "".join(res)

# Time Complexity: O(nlogk), we don't need to sort here, the most_common() cost O(nlogk) based on source code. In fact, the most_common used heapq on th implementation. Thus, we can consider this solution is the same as solution 2.
# Space Complexity: O(n)

# HashTable + Heap:
def frequencySort(self, s: str) -> str:
	# Count the occurence on each character
	cnt = collections.Counter(s)
	
	# Build heap
	heap = [(-v, k) for k, v in cnt.items()]
	heapq.heapify(heap)
	
	# Build string
	res = []
	while heap:
		v, k = heapq.heappop(heap)
		res += [k] * -v
	return ''.join(res)
# Time Complexity: O(nlogk), where k is the number of distinct character.
# Space Complexity: O(n)