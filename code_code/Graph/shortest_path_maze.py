# https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
from collections import deque
ROW = 9
COL = 10

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class queueNode:
    def __init__(self,pt, dist):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist 

def isValid(row, col):
    if (row >= 0 and row < ROW) and ( col >= 0 and col < COL):
        return True
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def BFS(m,src,dest):

    if m[src.x][src.y]!=1 or m[dest.x][dest.y]!=1:
        return -1

    visited = [[False for _ in range(COL)] for _ in range(ROW)]

    q = deque()
    # Distance of source cell is 0
    s = queueNode(src,0)
    q.append(s)

    while q:
        curr = q.popleft()
        pt = curr.pt

        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        
        visited[pt.x][pt.y] = True
        
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            if isValid(row, col) and m[row][col] == 1 and not visited[row][col]:
                adjCell = queueNode(Point(row,col), curr.dist + 1)
                q.append(adjCell)
    return -1

# Driver code
def main():
    mat = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
           [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
           [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
           [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
           [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
    source = Point(0,0)
    dest = Point(3,4)
     
    dist = BFS(mat,source,dest)
     
    if dist!=-1:
        print("Shortest Path is",dist)
    else:
        print("Shortest Path doesn't exist")
main()