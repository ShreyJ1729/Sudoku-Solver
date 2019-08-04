#Sudoku Solver
#How it works:
#Step One: User Input of Puzzle (0 means unsolved cell)
#Step Two: Preparation For Initial Reduction - New Grid made of possible numbers for every cell based on
#Step Three: Initial Reduction - If any cells have only one possibility, then they are replaced with it
#Step Four: Brute Force, speeded up with the initial reduction - A recursive approach is used with the g
#Step Five: If the recursion is complete and no valid solution has been found, print so. Else, print the
#Note: Example 5 was specifically designed to be difficult to brute force, and therefore it cant be solv
import sys
import math
import time
sys.setrecursionlimit(10000)
#Here is the Sudoku Below. It is a 9x9 grid formatted in Python as a list of 9 lists of numbers in the r
def PrintSudoku():
  for i in Sudoku:
    print(i)

#30 given numbers
example1 = [
[0, 0, 3, 0, 4, 2, 0, 9, 0],
[0, 9, 0, 0, 6, 0, 5, 0, 0],
[5, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 7, 0, 0, 2, 8, 5],
[0, 0, 8, 0, 0, 0, 1, 0, 0],
[3, 2, 9, 0, 0, 8, 7, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 5, 0, 9, 0, 0, 2, 0],
[0, 8, 0, 2, 1, 0, 6, 0, 0]
]
# 27 given numbers
example2 = [
[0, 0, 0, 0, 7, 0, 0, 0, 0],
[0, 7, 0, 2, 0, 3, 0, 9, 0],
[0, 0, 2, 0, 0, 0, 5, 0, 8],
[0, 6, 0, 0, 4, 0, 0, 5, 0],
[9, 0, 0, 1, 0, 7, 0, 0, 3],
[0, 1, 0, 0, 3, 0, 0, 6, 0],
[2, 0, 3, 0, 0, 0, 7, 0, 0],
[0, 8, 0, 3, 0, 9, 0, 1, 0],
[0, 0, 0, 0, 5, 0, 2, 0, 0]
]
#Hardest Classified Sudoku For Humans
example3 = [
[8, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 6, 0, 0, 0, 0, 0],
[0, 7, 0, 0, 9, 0, 2, 0, 0],
[0, 5, 0, 0, 0, 7, 0, 0, 0],
[0, 0, 0, 0, 4, 5, 7, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 3, 0],
[0, 0, 1, 0, 0, 0, 0, 6, 8],
[0, 0, 8, 5, 0, 0, 0, 1, 0],
[0, 9, 0, 0, 0, 0, 4, 0, 0]
]
#Another puzzle
example4 = [
[0, 4, 6, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 7, 2, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 8, 0],
[0, 0, 1, 0, 0, 3, 0, 7, 0],
[4, 0, 0, 0, 0, 6, 0, 0, 2],
[0, 2, 0, 0, 7, 0, 9, 1, 0],
[1, 0, 0, 8, 0, 0, 5, 0, 0],
[5, 0, 9, 4, 0, 2, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 4, 6, 0]
]

#Sudoku specifically desigend to be hard to brute force.
#This one is estimated to take ~155.8 hours through this program
example5 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 0, 8, 5],
[0, 0, 1, 0, 2, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 7, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 1, 0, 0],
[0, 9, 0, 0, 0, 0, 0, 0, 0],
[5, 0, 0, 0, 0, 0, 0, 7, 3],
[0, 0, 2, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 4, 0, 0, 0, 9]
]
#Example5 Flipped about the x axis. This one only takes ~3 minutes to solve.
example6 = [
[8, 0, 0, 0, 4, 0, 0, 0, 9],
[0, 0, 2, 0, 1, 0, 0, 0, 0],
[5, 0, 0, 0, 0, 0, 0, 7, 3],
[0, 9, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 5, 0, 7, 0, 0, 0],
[0, 0, 1, 0, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 0, 8, 5],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

SudokuInput = input("Enter Sudoku Grid as an Array of Rows. \nIf you want to use the example sudoku board enter example(n) without parenthesis for n={1, 2, 3, 4, 5, 6}.")
Sudoku = eval(SudokuInput)
print("\n\nYou have chose to solve the following sudoku grid:")
PrintSudoku()
print("\n\n\n")
start = time.time()
SudokuPossibilities = [
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
[[], [], [], [], [], [], [], [], []],
]
def SudokuRow(row):
  return Sudoku[row]

def SudokuColumn(column): #Abstraction
  SudokuSplice = []
  for i in Sudoku:
    SudokuSplice.append(i[column])
  return SudokuSplice

def Number(row, column):
  return Sudoku[row][column]

def PossibilitiesNumber(row, column):
  return Sudoku[row][column]

def NumberInRow(number, row):
  status = False
  for j in SudokuRow(row):
    if (j == number):
      status = True
  return status

def NumberInColumn(number, column):
  status = False
  for k in SudokuColumn(column):
    if (k == number):
      status = True
  return status

def NumberInNineSquare(bottomleftX, bottomleftY, number):
  SquareList = []
  for i in range(0, 3):
    for j in range(0, 3):
      SquareList.append(Number(bottomleftY+i, bottomleftX+j))
  if (SquareList.count(number) > 0):
    return True
  else:
    return False

def NineSquare(bottomleftX, bottomleftY):
  SquareList = []
  for i in range(0, 3):
    for j in range(0, 3):
      SquareList.append(Number(bottomleftY+i, bottomleftX+j))
  return SquareList

def RowValid(row):
  rowvalid = True
  for number in SudokuRow(row):
    if (SudokuRow(row).count(number)>1):
      rowvalid = False
  return rowvalid

def RowsValid():
  rowsvalid = True
  for row in range(0, 9):
    if (RowValid(row) == False):
      rowsvalid = False
  return rowsvalid

def ColumnValid(column):
  columnvalid = True
  for number in SudokuColumn(column):
    if (SudokuColumn(column).count(number)>1):
      columnvalid = False
  return columnvalid

def ColumnsValid():
  columnsvalid = True
  for column in range(0, 9):
    if (ColumnValid(column) == False):
      columnsvalid = False
  return columnsvalid

def NineSquareValid(bottomleftX, bottomleftY):
  squarevalid = True
  SquareList = NineSquare(bottomleftX, bottomleftY)
  for number in SquareList:
    if (SquareList.count(number)>1):
      squarevalid = False;
  return squarevalid

def NineSquaresValid():
  ninesquaresvalid = True
  for x in [0, 3, 6]:
    for y in [0, 3, 6]:
      if (NineSquareValid(x, y) == False):
        ninesquaresvalid = False
  return ninesquaresvalid

# Creates the Sudoku Possiblities list
def UpdateSudokuPossibilities():
  for row in range(9):
    for column in range(9):
      possibilities = []
      for number in range(1, 10):
        if (Sudoku[row][column] == 0 and NumberInRow(number, row) == False and NumberInColumn(number, column) and NumberInNineSquare(int(3*math.floor(column/3)), int(3*math.floor(row/3)), number) == False):
          possibilities.append(number)
        SudokuPossibilities[row][column] = possibilities

#Updates Sudoku Based on SudokuPosibilities and if there is only one element in a list of its list of li
def UpdateSudoku():
  for row in range(9):
    for column in range(9):
      if (len(SudokuPossibilities[row][column]) == 1):
        Sudoku[row][column] = SudokuPossibilities[row][column][0]

#Repeats updatesudoku and updatesudokupossibilities enough times to ensure discrete convergence
def ReduceSudoku():
  for i in range(10):
    UpdateSudoku()
    UpdateSudokuPossibilities()

def SquareValid(row, column, value):
  rowvalid = all([value != Sudoku[row][i] for i in range(9)])
  if rowvalid:
    columnvalid = all([value != Sudoku[i][column] for i in range(9)])
    if columnvalid:
      TopLeftX, TopLeftY = 3*math.floor(row/3), 3*math.floor(column/3)
      for x in range(TopLeftX, TopLeftX+3):
        for y in range(TopLeftY, TopLeftY+3):
          if Sudoku[x][y] == value:
            return False
      return True
  return False

def NextUnsolvedSquare(): #Child Algorithm
  for x in range(0,9):
    for y in range(0,9):
      if Sudoku[x][y] == 0:
        return x,y
  return -1,-1

def BruteForceSudoku(row=0, column=0): #Main Algorithm
  row,column = NextUnsolvedSquare()
  if (row == -1 and BoardValid()):
    return True
  for number in SudokuPossibilities[row][column]:
    if SquareValid(row,column,number):
      Sudoku[row][column] = number
      if BruteForceSudoku(row, column):
        return True
      Sudoku[row][column] = 0
  return False

def BoardValid(): #Child Algorithm
  if (RowsValid() == True and ColumnsValid() == True and NineSquaresValid() == True):
    return True
  else:
    return False

UpdateSudokuPossibilities()
ReduceSudoku()

print("Solving... Please Wait")

BruteForceSudoku()
end = time.time()

if BoardValid():
  print("Solution: \n")
  PrintSudoku()
  print("\nTime Taken: ", end - start, "seconds")
else:
  print("No Solution")
