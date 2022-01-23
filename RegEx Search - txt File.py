#RegEx Search - txt file
#Parse .txt file, extract specified data, covert data to float point, print maximum
import re
fhand = open('myexamplefile.txt')
#Define file handle, open specified file
numlist = list()
#Variable defined + var type defined 
for line in fhand: 
	line = line.rstrip()
	#Remove any trailing white spaces at end of string obj
	stuff = re.findall('^X-EXAMPLE-Confidence: ([0-9.]+)' ,line)
	#Seek lines beginning w/ spec substring, followed by nums/. >0
	#Filter/skip ("skip up") lines !=  defined specifications
	#Proceed on ("drop down") lines == defined specifications
	#Var stuff is extracted from substring(s) characterized by ([0-9.]+)
	if len(stuff) != 1: continue
	#If no lines matching, return empty list
	num = float(stuff[0])
	#Convert var stuff to floating point
	#Redefine var stuff --> "num" at index 0
	numlist.append(num)
	#Append var "num" to "numlist"
print('Maximum: ', max(numlist))
#Print and ID maximum val in var numlist