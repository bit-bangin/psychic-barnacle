# Accepting User Input - .txt file 

fname = input('Please enter a valid file name: ')
try: 
	fhand = open(fname)
except: 
	print('File: ', fname, 'cannot be opened.')
	exit()

