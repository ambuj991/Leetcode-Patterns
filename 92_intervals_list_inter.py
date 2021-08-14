# Complexity Analysis

# Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of A and B respectively.

# Space Complexity: O(M + N)O(M+N), the maximum size of the answer.

def intervalIntersection(firstList, secondList):
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            if a_start <= b_end and b_start <= a_end:
                res.append([max(a_start, b_start),  min(a_end, b_end)])
            if a_end <= b_end:
                i = i+1
            else:
                j = j+1
        return res
print(intervalIntersection( firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))