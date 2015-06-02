def getChar(mask):
	if (mask == 0):
		return '.'
	elif (mask == 1):
		return 'x'
	elif (mask == 2):
		return 'o'
	else:
		return '!'
class Board:
	winningPos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
	state = 0
	def toString(self):
		s = ""
		for i in range(3):
			for j in range(3):
				s += getChar(((self.state) >> (i * 3 * 2 + j * 2)) & 3)
			if (i < 2):
				s += '\n'
		return s
	def addMove(self, row, col, player):
		self.state = self.state | (player << (row * 2 * 3 + col * 2))
	def getState(self):
		return self.state
	def isOver(self):
		for player in range(1, 3):
			mask = 0
			for comb in self.winningPos:
				for i in comb:
					mask = (mask | (player << (i * 2)))
				if ((self.state & (mask)) == mask):
					return True
		return False