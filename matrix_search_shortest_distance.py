'''
given a 2D matrix of 1s and 0s where 0s are obstacles closed for traversing and 1s are paths to walk left, right, up, and down
find the shortest distsnce to reach a targer element in this 2D matrix from a given position such as top, left or (0,0)
'''

from collections import defaultdict 
import heapq

visited = set()        
paths = defaultdict(list)
min_heap = []

def get_coordinates(pos, left, right, top, down, lot):
    coordinates = []
    row, col = pos[0], pos[1]
    if left and lot[row][col-1] != 0:
        coordinates.append((row, col-1))
    if right and lot[row][col+1] != 0:
        coordinates.append((row, col+1))
    if top and lot[row-1][col] != 0:
        coordinates.append((row-1, col))
    if down and lot[row+1][col] != 0:
        coordinates.append((row+1, col))
    return coordinates    

def get_peers(pos, numRow, numCol, lot):
    left, right, top, down = None, None, None, None
    row, col = pos[0], pos[1]
    if row > 0 and col > 0 and row < numRow-1 and col < numCol-1:
        left, right, top, down = 1,1,1,1
    if row > 0 == 0:
        top = 1
    if row < numRow - 1:
        down = 1
    if col < numCol - 1:
        right = 1 
    if col > 0:
        left = 1
    peers = get_coordinates(pos, left, right, top, down, lot)
    unique_peers = [peer for peer in peers if peer not in visited]
    return unique_peers
        
def traverse(row, col, numRow, numCol, lot, target, distance):
    pos = (row, col)
    visited.add(pos)                                # put current position in set of visited positions
    peers = get_peers(pos, numRow, numCol, lot)     # get all valid peers/neighboors for current position
    found = 0
    for peer in peers:                              # check is any of the currenct pos's peers are the target
        if lot[peer[0]][peer[1]] == target:
            heapq.heappush(min_heap, distance+1)    # if targer is found, put it in a min heap
            found = 1                               # and continue looking for even shorter paths 
            
        else:                       # even if this peer is not the targer, it might be a path to the target
            paths[pos].append(peer)

    while paths[pos]:       # go deep into each possible paths towards the target from the current position
        loc = paths[pos].pop()
        traverse(loc[0], loc[1], numRow, numCol, lot, target, distance+1)              
    distance -= 1           # if all paths of current position does Not lead to the targer OR there are no paths,
    if found: distance += 1 # deduct distance travelled by 1 and go backwards (by way of recursion stack recoil)
    return 

def robo_track(numRow, numCol, lot, target=9, start_row=0, start_col=0, opened=1, closed=0):
    if lot[start_row][start_col] == target:
        return 0
    if lot[start_row][start_col] == opened:
        traverse(start_row, start_col, numRow, numCol, lot, target, distance=0)
    if len(min_heap):
        return heapq.heappop(min_heap)
    return -1
                                           
#input array
lot = [[1, 0, 1],
     [1, 0, 1],
     [1, 9, 1]]

mat=[[1, 1, 0, 1, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 0],
     [1, 1, 0, 1, 0, 1, 0],
     [9, 1, 0, 9, 1, 1, 0],
     [0, 9, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 0, 1, 1]]
result = robo_track(len(lot), len(lot[0]), lot) 
#result = robo_track(len(mat), len(mat[0]), mat)
print(result)
