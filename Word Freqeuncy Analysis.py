# Open .txt file

fhand = open('mytextfile.txt')

# Reading file & computes dictionary

counts = dict()
for line in fhand: 
	line = line.translate(str.maketrans('','', string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words: 
		if word not in counts: 
			counts[word] = 1
		else: 
			counts[word] +=1

# Construct list of tuples for sorting

mylist = list()
for key, val in list(counts.items()): 
	mylist.append((val,key))

# Reverse sort

mylist.sort(reverse=True)

# Output most used 

for key,val in mylist [:10]: 
	print(key,val)