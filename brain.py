class Brain:
	winningPos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
	posEval = {}
	checked = {}
	moves = {}
	player = 0
	def __init__(self, player):
		self.player = player
		print("Thinking...")
		for i in range(1 << 18):
			self.checked[i] = False
			self.moves[i] = [-1, -1]
		for i in range(1 << 18):
			isFull = True
			for j in range(9):
				if (((i >> (2 * j)) & 3) == 0):
					isFull = False
			if (isFull):
				self.checked[i] = True
				self.posEval[i] = 1
			for comb in self.winningPos:
				mask = 0
				for j in comb:
					mask = (mask | (self.player << (2 * j)))
				if ((i & mask) == mask):
					self.checked[i] = True
					self.posEval[i] = 2
				mask = 0
				for j in comb:
					mask = (mask | ((self.player ^ 3) << (2 * j)))
				if ((i & mask) == mask):
					self.checked[i] = True
					self.posEval[i] = 0
		self.evalPos(0, 1)
	def getNextMove(self, board):
		return self.moves[board]
	def evalPos(self, board, turn):
		if (self.checked[board]):
			return self.posEval[board]
		if (turn == self.player):
			choice = -1
			for i in range(3):
				for j in range(3):
					if (((board >> (i * 2 * 3 + j * 2)) & 3) == 0):
						curChoice = self.evalPos(board | (self.player << (i * 2 * 3 + j * 2)), turn ^ 3)
						if (choice < curChoice):
							choice = curChoice
							self.moves[board][0] = i
							self.moves[board][1] = j
			self.checked[board] = True
			self.posEval[board] = choice
		else:
			choice = 3
			for i in range(3):
				for j in range(3):
					if ((board >> ((i * 2 * 3 + j * 2)) & 3) == 0):
						curChoice = self.evalPos(board | (turn << (i * 2 * 3 + j * 2)), turn ^ 3)
						if (choice > curChoice):
							choice = curChoice
							self.moves[board][0] = i
							self.moves[board][1] = j
			self.checked[board] = True
			self.posEval[board] = choice
		return self.posEval[board]