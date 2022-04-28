# https://leetcode.com/problems/path-with-minimum-effort/
# Heapq module, sort with first element
# min heap is a binary tree in which the parent nodes hold smaller values than that of the children.  
# heapq.heapify(heapData) ; heapq.heappush(heapData, 40)
    # p = [(30,2,0),(20,1,0),(10,0,0)]
    # heapq.heapify(p)
    # print(p)

## method 1: Dijkstra's algorithm
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        
        def notOutOfRange(i,j):
            return (0 <= i < row) and (0 <= j < col)
        
        pq = [(0,0,0)] # (effort, row, col)
        # cannot heapfily(list to heap), then pq cannot be iterated
        
        efforts = [[math.inf]*col for r in range(row)]
        efforts[0][0] = 0 # no effort at starting point
        # print(efforts)
        
        while pq:
            e, r, c = heapq.heappop(pq)
            # print(e,r,c)
            if e > efforts[r][c]:
                continue # don't save and don't use this to reach other nodes as it's not the least effort
            else:
                # check effort from current node to up/down/left/right
                for dir_r, dir_c in [[1,0],[0,1],[-1,0],[0,-1]]:
                    # if not out of range
                    if notOutOfRange(r+dir_r, c+dir_c):
                        # because we are recording so far max step, so max(cur, max so far)
                        new_e = max(abs(heights[r][c]-heights[r+dir_r][c+dir_c]),e)
                        # but we want a min max step
                        if new_e < efforts[r+dir_r][c+dir_c]:
                            efforts[r+dir_r][c+dir_c] = new_e
                            heapq.heappush(pq, (efforts[r+dir_r][c+dir_c],r+dir_r,c+dir_c))
                                    
                print(efforts)
        return efforts[-1][-1]
                    
            
            