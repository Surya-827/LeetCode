class MinStack:
	minsStack = []
	valuesStack = []

	def __init__(self):
		self.minsStack = []
		self.valuesStack = []

	def push(self, val: int) -> None:
		if not self.minsStack and not self.valuesStack:
			self.valuesStack.append(val)
			self.minsStack.append(val)
		else:
			self.valuesStack.append(val)

			if val <= self.minsStack[-1]:
				self.minsStack.append(val)

	def pop(self) -> None:
		last_val = self.valuesStack.pop()

		if last_val == self.minsStack[-1]:
			self.minsStack.pop()

	def top(self) -> int:
		return self.valuesStack[-1]

	def getMin(self) -> int:
		return self.minsStack[-1]