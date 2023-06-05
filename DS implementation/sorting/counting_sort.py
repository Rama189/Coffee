def c_sort(nums):
    k = max(nums)
    l = len(nums)
    occ_arr = [0] * (k + 1)
    sorted_arr = [0] * (l)

    for x in nums:
        occ_arr[x] += 1

    for i in range(1, len(occ_arr)):
        occ_arr[i] += occ_arr[i - 1]
    
    for num in nums:
        sorted_arr[occ_arr[num]-1] = num
        occ_arr[num] = occ_arr[num]-1
    
    return sorted_arr

if __name__ == "__main__":
    s_arr = c_sort([3,4,2,1,0, 18, 16, 13, 20, 22, 19, 19, 13])
    print(s_arr)