class Solution:
    def merge(self, intervals):
      
        intervals.sort()
        output = [intervals[0]] 
        
        for s, e in intervals[1: ]:
            last = output[-1][1]
            if last >= s:
                output[-1][1] = max(last, e)
            else:
                output.append([s, e])
        return output
                
       