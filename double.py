def doubler(func):
	def call_twice():
		func()
		func()
	return call_twice

@doubler
def printer():
	print("foo")

printer()
