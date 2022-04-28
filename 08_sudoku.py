# https://leetcode.com/problems/valid-sudoku/submissions/
## method 1: 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet).
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        square=collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in square[(r//3, c//3)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True
                    
## method 2: 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = []
        # chehck row and turn str list to int
        for row in board:
            r = [int(x) if x is not "." else 0 for x in row]
            for i, y in enumerate(r):
                if y != 0 and (y not in range(1,10) or y in r[:i]):
                    print('y1 {}, i1 {},row {}'.format(y,i,r))
                    return False
            b.append(r)
        print(b)
        # map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
        # zip() function is defined as zip(*iterables). The function takes in iterables as arguments and returns an iterator
        b_col = list(map(list, zip(*b)))
        print(b_col)
        
        # chehck col
        for r in b_col:
            for i, y in enumerate(r):
                if y != 0 and (y not in range(1,10) or y in r[:i]):
                    print('y2 {}, i2 {}, r[:i2] {}, row {}'.format(y,i,r[:i],r))
                    return False
                
        # chehck 3x3
        top_left = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for [i,j] in top_left:
            grid = []
            for m in [0,1,2]:
                for n in [0,1,2]:
                    if b[i+m][j+n]!=0 and b[i+m][j+n] in grid:
                        return False
                    grid.append(b[i+m][j+n])
            print(grid)
        return True
    
        