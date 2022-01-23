#Double Split Pattern 
datastr = "From example.email@uct.ac.za Sat Jan 1 09:14:18 2000"
#"Split" string object at spaces
words = line.split()
#Return [0-'From'][1-'example.email@uct.ac.za'][2-'Sat'][3'Jan']
#[4-'1'][5-'09:14:18'][6-'2000']
#Access newly split datstr at index position 1
email = words [1]
#Return [1-'example.email@uct.ac.za']
#"Split" string object at the '@'
pieces = email.split('@')
print(pieces[1])