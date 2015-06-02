class Board:
	state = 0
	def getChar(self, mask):
		if (mask == 0):
			return '.'
		elif (mask == 1):
			return 'x'
		elif (mask == 2):
			return 'o'
		else:
			return '!'
	def toString(self):
		s = ""
		for i in range(3):
			for j in range(3):
				s += getChar(((self.state) >> (i * 3 * 2 + j * 2)) & 3)
		return s
	def addMove(self, row, col, player):
		self.state = self.state | (player << (row * 2 * 3 + col * 2))

