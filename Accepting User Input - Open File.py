# Accepting User Input - .txt file 
def accept_user_input(fname):
	'''
	Function to accept user input.
	Incorporation of exception handling to prevent malfunction. 
	'''
	fname = input('Please enter a valid file name: ')
	try: 
		fhand = open(fname)
	except: 
		print('File: ', fname, 'cannot be opened.')
		exit()

