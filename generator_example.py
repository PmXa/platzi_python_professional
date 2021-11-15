def my_generator():
	"""Ejemplo de un generador"""
	
	print("Hello, world!")
	n = 0
	yield n
	
	print("Hello, heaven!")
	n = 1
	yield n
	
	print("Hello, hell!")
	n = 2
	yield n


# ---------------------------
# Main function & entry point
# ---------------------------

def run():
	x = my_generator()
	
	print(next(x)) # Hello, world!
	print(next(x)) # Hello, heaven!
	print(next(x)) # Hello, hell!
	# print(next(x)) # StopIteration

	my_list = [0,1,4,7,14,17,24,40,44,57]

	square_list = [x**2 for x in my_list]
	square_gen = (x**2 for x in my_list)

	print(next(square_gen)) # 0 
	print(next(square_gen)) # 1
	print(next(square_gen)) # 16


if __name__ == '__main__':
    run()