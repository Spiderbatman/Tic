from board import Board
from brain import Brain

board = Board()
brain = Brain(2)

turn = 1

while (not board.isOver()):
	print(board.getState())
	if (turn == 1):
		row = raw_input("Enter row ")
		col = raw_input("Enter column ")
		board.addMove(int(row), int(col), turn)
		print(board.toString())
		print("------------------")
	else:
		nextMove = brain.getNextMove(board.getState())
		print(nextMove)
		board.addMove(nextMove[0], nextMove[1], turn)
		print(board.toString())
		print("------------------")
	turn = turn ^ 3
print("Game Over")
print("Player " + (i ^ 3) + " won")

