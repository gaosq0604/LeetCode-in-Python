class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for item in nums[k:]:
            # if item > heap[0]:
                # heapq.heapreplace(heap, item)
            heapq.heappushpop(heap, item)
        return heap[0]
    
    '''def partition(self, xs, lo, hi):
        mid = lo + (hi-lo)//2
        xs[mid], xs[hi] = xs[hi], xs[mid]
        # invariant:
        #
        #   xs[j] <= xs[hi] for all j <= i
        #   xs[j] >  xs[hi] for all j >  i
        i = lo
        for j in range(lo, hi):
            if xs[j] <= xs[hi]:
                xs[j], xs[i] = xs[i], xs[j]
                i += 1
        xs[i], xs[hi] = xs[hi], xs[i]
        return i

    def findKthLargest(self, xs, k):
        # kth largest element in O(n) time and O(1) space.
        n = len(xs)
        lo, hi = 0, n-1
        while lo <= hi:
            p = self.partition(xs, lo, hi)
            if p == n-k:
                return xs[p]
            elif p < n-k:
                lo = p+1
            else:
                hi = p-1
        raise ValueError(xs, k)'''