y = 4

def func_counter(func):
	count = 0
	def count_tracker(y):
		func(y)
	count += 1
	return count_tracker

@func_counter
def foo(y):
	return y+2*3-34

foo(y)
foo(y)
print(foo.counter)
