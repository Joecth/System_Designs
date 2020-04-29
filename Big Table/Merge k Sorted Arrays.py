# 486. Merge K Sorted Arrays
# 中文English
# Given k sorted integer arrays, merge them into one sorted array.

# Example
# Example 1:

# Input: 
#   [
#     [1, 3, 5, 7],
#     [2, 4, 6],
#     [0, 8, 9, 10, 11]
#   ]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Example 2:

# Input:
#   [
#     [1,2,3],
#     [1,2]
#   ]
# Output: [1,1,2,2,3]
# Challenge
# Do it in O(N log k).

# N is the total number of integers.
# k is the number of arrays.


import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        return self.helper_heapq(arrays)
        
    def helper_heapq(self, arrays):
        hp = []
        for k in range(len(arrays)):
            if not arrays[k]: continue
            heapq.heappush(hp, (arrays[k][0], k, 0))
            
        # print(hp)
        res = []
        while hp: 
            _, kth, idx = heapq.heappop(hp)
            # print(val, arrays[kth][idx], kth, idx)
            res.append(arrays[kth][idx])
            if idx+1 <= len(arrays[kth])-1:
                heapq.heappush(hp, (arrays[kth][idx+1], kth, idx+1))
            # else:
            # 大可以等下一輪拉出來再push那條的下一個元素，不急
            #     # while idx+1 > len(array[kth])-1:
            #     val, kth, idx = heapq.heappop(hp)
            #     res.append(val)
        return res