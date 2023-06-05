def bin_search(l, h, arr, t):
    while l <= h:
        m = l + (h - l) // 2
        print(m)
        if arr[m] == t:
            return m
        elif arr[m] > t:
            h = m - 1
        else:
            l = m + 1
    return -1

# Driver function
def findPos(arr,t):
    l = 0
    h = 1

    while t > arr[h]:
        temp = h + 1
        h = h + (h - l + 1) * 2
        l = temp
        print(l,h,t)
    return bin_search(l, h, arr,  t)


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = findPos(arr,10)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)