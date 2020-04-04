# 在 Consistent Hashing I 中我们介绍了一个比较简单的一致性哈希算法，这个简单的版本有两个缺陷：

# 增加一台机器之后，数据全部从其中一台机器过来，这一台机器的读负载过大，对正常的服务会造成影响。
# 当增加到3台机器的时候，每台服务器的负载量不均衡，为1:1:2。
# 为了解决这个问题，引入了 micro-shards 的概念，一个更好的算法是这样：

# 将 360° 的区间分得更细。从 0~359 变为一个 0 ~ n-1 的区间，将这个区间首尾相接，连成一个圆。
# 当加入一台新的机器的时候，随机选择在圆周中撒 k 个点，代表这台机器的 k 个 micro-shards。
# 每个数据在圆周上也对应一个点，这个点通过一个 hash function 来计算。
# 一个数据该属于哪台机器负责管理，是按照该数据对应的圆周上的点在圆上顺时针碰到的第一个 micro-shard 点所属的机器来决定。
# n 和 k在真实的 NoSQL 数据库中一般是 2^64 和 1000。

# 请实现这种引入了 micro-shard 的 consistent hashing 的方法。主要实现如下的三个函数：

# create(int n, int k)
# addMachine(int machine_id) // add a new machine, return a list of shard ids.
# getMachineIdByHashCode(int hashcode) // return machine id
# Example
# 样例 1:

# 输入:
#   create(100, 3)
#   addMachine(1)
#   getMachineIdByHashCode(4)
#   addMachine(2)
#   getMachineIdByHashCode(61)
#   getMachineIdByHashCode(91)
# 输出: 
#   [77,83,86]
#   1
#   [15,35,93]
#   1
#   2
# 样例 2:

# 输入: 
#   create(10, 5)
#   addMachine(1)
#   getMachineIdByHashCode(4)
#   addMachine(2)
#   getMachineIdByHashCode(0)
#   getMachineIdByHashCode(1)
#   getMachineIdByHashCode(2)
#   getMachineIdByHashCode(3)
#   getMachineIdByHashCode(4)
#   getMachineIdByHashCode(5)
# 输出: 
#   [2,3,5,6,7]
#   1
#   [0,1,4,8,9]
#   2
#   2
#   1
#   1
#   2
#   1
# Notice

from collections import deque
from math import ceil, log
class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        # write your code here
        Q = deque()
        v = [0, 359, 1]
        Q.append(v)
        res = Q
        for idx in range(1, n):
            cur = idx + 1
            low, high, idx = Q.popleft()

            Q.append([low , (low+high)//2, idx])
            new_v = [(low+high)//2+1 , high,cur]
            Q.append(new_v)
            res = Q
            
            ## Following makes system use smaller ID for same size segs, but still failed at 76, Anyway, sequence matters less
            if not self.is_power_of_two(cur):
                len_to_sort = 2**ceil(log(cur,2)) - cur
                tmp = sorted(list(Q)[:len_to_sort], key=lambda x: x[2])
                # print('tmp: ', tmp)
                tmp.extend(list(Q)[len_to_sort:])
                Q = deque(tmp)
                # print('Q: ', Q)

        return list(res)
    
    def is_power_of_two(self, n):
        return not (n & (n-1))

if __name__ == '__main__':
    sol = Solution()
    sol.consistentHashing(3)