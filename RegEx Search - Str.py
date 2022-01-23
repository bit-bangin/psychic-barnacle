#RegEx Search 
import re
datastr = 'From myexample.email@uct.ac.za Sat Jan 5 09:14:16 2000'
y = re.findall('^From .*@([^ ]*)' ,datastr)
#Seek on lines starting with "From " + any num of non whitespace char + @
#Capturing/Extracting/Grouping a Set of repeating non whitespace char
print(y)