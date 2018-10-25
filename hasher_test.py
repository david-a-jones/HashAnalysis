from hasher import *

#number of buckets
m = int(input('Number of buckets: '))

#do an insertion of all the elements in a list into a dictionary
def getKeySet(S):
	K = []
	for item in S:
		K.append(modHash(item, m))
	return K

#parse a text document and store its content in a list (the words must be separated by newlines)
def listFromParse(filename):
	wordSet = []
	fin = open(filename)
	for line in fin:
		wordSet.append(line)
	return wordSet
	
#given a list of keys, return a sorted list where F[i] = the frequency of the key i
def getKeyFrequencies(K):
	fList = []
	for key in range(m):
		fList.append(0)
	#do a second pass to use indices to increment
	for key in K:
		fList[key] = fList[key] + 1
	return fList
	
wordSet = listFromParse('word-list.txt')
keySet = getKeySet(wordSet)
frequencyList = getKeyFrequencies(keySet)

#output the list to a file
outName = 'frequency_mod_' + str(m) + '.txt'
outFile = open(outName,'w+')
for f in frequencyList:
	outFile.write(str(f)+'\n')
