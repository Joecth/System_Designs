# Implement a simple client for GFS (Google File System, a distributed file system), it provides the following methods:

# read(filename). Read the file with given filename from GFS.
# write(filename, content). Write a file with given filename & content to GFS.
# There are two private methods that already implemented in the base class:

# readChunk(filename, chunkIndex). Read a chunk from GFS.
# writeChunk(filename, chunkIndex, chunkData). Write a chunk to GFS.
# To simplify this question, we can assume that the chunk size is chunkSize bytes. (In a real world system, it is 64M). The GFS Client's job is splitting a file into multiple chunks (if need) and save to the remote GFS server. chunkSize will be given in the constructor. You need to call these two private methods to implement read & write methods.

# Example
# GFSClient(5)
# read("a.txt")
# >> null
# write("a.txt", "World")
# >> You don't need to return anything, but you need to call writeChunk("a.txt", 0, "World") to write a 5 bytes chunk to GFS.
# read("a.txt")
# >> "World"
# write("b.txt", "111112222233")
# >> You need to save "11111" at chunk 0, "22222" at chunk 1, "33" at chunk 2.
# write("b.txt", "aaaaabbbbb")
# read("b.txt")
# >> "aaaaabbbbb"

##Calling
# GFSClient(5)
# read("a.txt")
# write("a.txt", "World")
# read("a.txt")
# write("b.txt", "111112222233")
# read("b.txt")
# write("b.txt", "aaaaabbbbb")
# read("b.txt")


# CURRENTLY STILL FAILED AT THE FOLLOWING CASE... SHOULD BE CONCEPT ISSUE...
"""
INPUT:
GFSClient(12)
read("access.log")
write("access.log", "/problem/en/a/problem/en/a-b-problem//problem/en/a-b-problem/")
read("access.log")
write("access_1.log", "testtesttest")
read("access_1.log")
write("access.log", "111111111111111122222222222222222223333333333333333")
read("access.log")
write("access.log", "1")
write("access.log", "2")
write("access.log", "3")
read("access_1.log")
read("access.log")
read("access_2.log")
write("access_1.log", "123")
write("access_1000.log", "111111111111111122222222222222222223333333333333444444444444444444444442222222222222222222222333")
read("access_1000.log")

Output
null
"/problem/en/a/problem/en/a-b-problem//problem/en/a-b-problem/"
"testtesttest"
"111111111111111122222222222222222223333333333333333"
null
"123"
null
"111111111111111122222222222222222223333333333333444444444444444444444442222222222222222222222333"

Expected
null
"/problem/en/a/problem/en/a-b-problem//problem/en/a-b-problem/"
"testtesttest"
"111111111111111122222222222222222223333333333333333"
&quot;testtesttest"
"3"
null
"111111111111111122222222222222222223333333333333444444444444444444444442222222222222222222222333"

"""

'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''

from collections import defaultdict
class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        # do intialization if necessary
        # BaseGFSClient.__init__(self)
        # initialize your data structure here
        self.chunkSize = chunkSize
        # self.chunkIndex = 0 　# 不同的chunk該有不同的Index在維護
        self.chunkIndexes = defaultdict(list)   
                                        # 應該是一個file會對應到很多個chunk
                                        # a.txt [0 ]
                                        # b.txt [0 1 2]
        super().__init__()
        self.seek = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        # write your code here
        tmp = self.seek.get(filename, 0)
        ret = ''
        while tmp < len(self.chunkIndexes[filename]):
            content = self.readChunk(filename, self.chunkIndexes[filename][tmp])
            if content:
                ret += content
            tmp += 1
        self.seek[filename] = tmp
        # self.chunkIndexes[filename] = tmp
        return ret if ret else None
            

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # write your code here
        i_cont = 0
        
        cur_ck_idx = 0 if not self.chunkIndexes[filename] else self.chunkIndexes[filename][-1]+1
        
        while i_cont < len(content):
            self.chunkIndexes[filename] += [cur_ck_idx]
            self.writeChunk(filename, cur_ck_idx, content[i_cont:i_cont+self.chunkSize])
            # print(self.readChunk(filename, cur_ck_idx))
            cur_ck_idx += 1
            i_cont += self.chunkSize


# STANDARD ANSWER:
# '''
# Definition of BaseGFSClient
# class BaseGFSClient:
#     def readChunk(self, filename, chunkIndex):
#         # Read a chunk from GFS
#     def writeChunk(self, filename, chunkIndex, content):
#         # Write a chunk to GFS
# '''
# class GFSClient(BaseGFSClient):

#     # @param {int} chunkSize chunk size bytes
#     def __init__(self, chunkSize):
#         BaseGFSClient.__init__(self)
#         # initialize your data structure here
#         self.chunkSize = chunkSize
#         self.chunkNum = dict()


#     # @param {str} filename a file name
#     # @return {str} conetent of the file given from GFS
#     def read(self, filename):
#         # Write your code here
#         if filename not in self.chunkNum:
#             return None
#         content = ''
#         for index in xrange(self.chunkNum.get(filename)):
#             sub_content = BaseGFSClient.readChunk(self, filename, index)
#             if sub_content:
#                 content += sub_content

#         return content


#     # @param {str} filename a file name
#     # @param {str} content a string
#     # @return nothing
#     def write(self, filename, content):
#         # Write your code here
#         length = len(content)
#         chunkNum = (length - 1) / self.chunkSize + 1
#         self.chunkNum[filename] = chunkNum
#         for index in xrange(chunkNum):
#             sub_content = content[index * self.chunkSize :
#                                   (index + 1) * self.chunkSize]
#             BaseGFSClient.writeChunk(self, filename, index, sub_content)