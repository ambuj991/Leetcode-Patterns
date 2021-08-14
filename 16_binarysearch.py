def solve(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        print(low, high)
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

l = list(map(int, input().split()))
a = int(input())
print(solve(l,a ))

# Time complexity : O(log n)
