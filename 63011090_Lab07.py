import time
def printBoard(b):
    print(b)

def putQueen(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N): # ใล่ใส่ไปทีละ column ทุก col.
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: #ใส่ได้?
            b[r] = c    # ใส่ ที่ r, c

            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 # เปลี่ยน data struct ไม่ให้ใส่แนวนี้

            if r == N-1:       # ถ้าใส่ควีนครบแล้ว
                #printBoard(b)  #print(b)
                numSol += 1
            else:
                putQueen(r+1, b, colFree, upFree, downFree)  # ใส่ควีนแถวถัดไป
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 #เอา Queen ออกเพื่อให้ได้ solution อื่น
                                                             # หรือ เพราะ queen ตัวนี้แม้ใส่ได้แต่ไม่ทำให้เกิด solution

	
class nQueen_interative:
    def __init__(self, size):
        self.size = size
        self.columns = []
 
    def place_in_next_row(self, column):
        self.columns.append(column)
 
    def remove_in_current_row(self):
        return self.columns.pop()
 
    def is_this_column_safe_in_next_row(self, column):
        row = len(self.columns)

        for queen_column in self.columns:
            if column == queen_column:
                return False
 
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
 
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
 
        return True
 

 
 
def solve_queen(size):
    board = nQueen_interative(size)
    number_of_solutions = 0
 
    row = 0
    column = 0
    while True:
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1
 
        if (column == size or row == size):
            if row == size:
                number_of_solutions += 1

                board.remove_in_current_row()
                row -= 1
 
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:
                break
            row -= 1
            column = 1 + prev_column
 
    return number_of_solutions
n = 4
print(' n |                iterative                      |                recursive                      |'.format(n))
print('   |           sol     |               time(sec)   |           sol     |               time(sec)   |'.format(n))
while n <=14:
    start_time = time.time()
    sol_iter = solve_queen(n)
    time_iterative = time.time() - start_time

    start_time = time.time()
    N = n    # N x N Board 
    numSol = 0     # number of solutions
    b = N*[-1]     # indices =S rows, b[index] = coloumn, first init to -1
    colFree = N*[1]    # all N col are free at first    
    upFree = (2*N - 1)*[1]   # all up diagonals are free at first
    downFree = (2*N - 1)*[1]      # all down diagonals are free at first
    putQueen(0, b, colFree, upFree, downFree) 
    time_recursive = time.time() - start_time

    print('{:2} | {:16}  |  {:20.4f}     | {:16}  |  {:20.4f}     |'.format(n, sol_iter,time_iterative,numSol,time_recursive,))
    n += 1

