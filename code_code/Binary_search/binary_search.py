def binary_search(array, target):
    # Define interval
    # Close interval [lo, hi] in this case
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if array[mid] == target:
            return mid, lo
        elif array[mid] > target:
            hi = mid - 1
        elif array[mid] < target:
            lo = mid + 1

    # Do something when we reach empty interval
    return -1, lo

k, low = binary_search([2,3,9,10,11], 5)
print(k, low)