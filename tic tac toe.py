# Constants
EMPTY = "."
X     = "X"
O     = "O"

def is_valid(row, col):
  return (
    row >= 0 and row < 3 and
    col >= 0 and col < 3   )

def at(row, col):
  return row * 3 + col

def draw(board):
  print("  A B C")
  for row in range(3):
    print(row + 1, end = " ")
    for col in range(3):
      print(board[at(row, col)], end = " ")
    print()

def where(where):
  where = where.upper()
  row = ord(where[1]) - ord("1")
  col = ord(where[0]) - ord("A")
  return row, col

def put(board, row, col, what):
  if is_valid(row, col):
    board[at(row, col)] = what

def get(board, row, col):
  return board[at(row, col)] if is_valid(row, col) else None

def get_row(board, row):
  return [
    get(board, row, 0),
    get(board, row, 1),
    get(board, row, 2)
  ]

def get_col(board, col):
  return [
    get(board, 0, col),
    get(board, 1, col),
    get(board, 2, col)
  ]

def get_d1(board):
  return [
    get(board, 0, 0),
    get(board, 1, 1),
    get(board, 2, 2)
  ]

def get_d2(board):
  return [
    get(board, 2, 0),
    get(board, 1, 1),
    get(board, 0, 2)
  ]

def is_empty(board, row, col):
  return get(board, row, col) == EMPTY

def is_x(board, row, col):
  return get(board, row, col) == X

def is_o(board, row, col):
  return get(board, row, col) == O

def count(run, symbol):
  count = 0
  for r in run:
    if r == symbol:
      count += 1
  return count

def check_rows(board):
  for row in range(3):
    if count(get_row(board, row), X) == 3: return X
    if count(get_row(board, row), O) == 3: return O

def check_cols(board):
  for col in range(3):
    if count(get_col(board, col), X) == 3: return X
    if count(get_col(board, col), O) == 3: return O

def check_diagnols(board):
  if count(get_d1(board), X) == 3: return X
  if count(get_d2(board), O) == 3: return O

def check(board):
  winner = check_rows(board)
  if winner: return winner
  winner = check_cols(board)
  if winner: return winner
  winner = check_diagnols(board)
  if winner: return winner

def play():
  board = [ EMPTY ] * 9
  turn = 0
  while True:
    print()
    draw(board)
    print()

    if turn > 4:
      winner = check(board)
      if winner == X: 
        input("Player 1 wins!")
        board = [ EMPTY ] * 9
        turn = 0
        continue
      if winner == O: 
        input("Player 2 wins!")
        board = [ EMPTY ] * 9
        turn = 0
        continue
      if turn   == 9: 
        input("Cat's Game!")
        board = [ EMPTY ] * 9
        turn = 0
        continue

    match turn & 1:
      case 0: turn = x_turn(board, turn)
      case 1: turn = o_turn(board, turn)

def x_turn(board, turn):
  print("It is Player 1's turn.")
  while True:
    move = input("What is your move? ")
    if is_empty(board, *where(move)):
      put(board, *where(move), X)
      return turn + 1
    else:
      print("That move is unavailable...")


def o_turn(board, turn):
  print("It is Player 2's turn.")
  while True:
    move = input("What is your move? ")
    if is_empty(board, *where(move)):
      put(board, *where(move), O)
      return turn + 1
    else:
      print("That move is unavailable...")

play()