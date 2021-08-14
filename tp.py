import collections

def leastInterval( tasks, n: int) -> int:
        c = collections.Counter(tasks)
        ct  = 0
        for i in c:
            ct  += c[i] * n if c[i]%2==0 else (c[i]-1)*n
        return ct

print(leastInterval( tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))