class Example:
	def __init__(self, x):
		self.x = x
	@property
	def ys(self):
		return self.x * 100

exemplar = Example(10)
exemplar.x = 112
print(exemplar.ys)