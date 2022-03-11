import time

def calculate_time(func):
	def display_time():
		start_time = time.time()
		func()
		end_time = time.time()
		print(f'Total time {end_time-start_time}')
	return display_time

@calculate_time
def timer():
	print("Hello World")

timer()
