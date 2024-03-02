import sys
import re

print ("Opening file...")
file = open ('/Users/prashanth/Downloads/logs.txt')
print ("Opening file complete...")


words = ['campaign id  ====> ','imported campaignProperties size ====>']

# read all lines in a list 
lines = file.readlines()
for line in lines:
	# print('Line:', line)
	 # check if string present on a current line
	for word in words:
		if line.find(word) != -1:
			# print(word, 'string exists in file')
			# print('Line Number:', lines.index(line))
			print('Line:', line)
			# print(line[44:48]+",", end =" ")

print(" ")