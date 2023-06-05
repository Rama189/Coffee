def floorSearch(arr, l, hi, x):
    # l = 0
    # hi = len(arr) - 1
    res = -1
    while(l <= hi):
        mid = l + (hi - l) // 2
        if arr[mid] <= x:
            res = arr[mid]
            l = mid + 1
        else:
            hi = mid - 1

    return res


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 4, 6, 10, 12, 14]
    n = len(arr)
    x = 7
 
    # Function call
    index = floorSearch(arr, 0, n-1, x)
 
    if (index == -1):
        print("Floor of", x, "doesn't exist\
                      in array ", end="")
    else:
        print("Floor of", x, "is", index)