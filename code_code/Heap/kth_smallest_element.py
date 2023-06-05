class MaxHeap:
    # Constructor
    def __init__(self, a, size):
        self.harr = a
        # maximum possible size of max heap
        self.capacity = None
        # current number of elements in max heap
        self.heap_size = size

def kthSmallest(arr, N, K):
    # Build a heap of first k elements in O(k) time
    mh = MaxHeap(arr, K)

# Driver's code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 4
 
    # Function call
    print("K'th smallest element is", kthSmallest(arr, N, K))