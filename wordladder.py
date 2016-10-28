import json
import pprint 

from collections import defaultdict
from collections import deque
from itertools import product

def getWords(lengthOfStartWord, startWord, endWord):
	results = []
	#open dictionary and read data (word of size = size of start/end word)
	with open('dictionary.json') as jsonData:
		data = json.load(jsonData)
		word = sorted(data.keys())
		results += word
		wordCount = 0
		graphWords = []
		for result in results:
			if (len(result) == lengthOfStartWord):
				wordCount +=1
				graphWords.append(result)

				if (result == startWord):
					print('Start word exists')
				if (result == endWord):
					print('End word exists')
				

	return (graphWords)	

def buildGraphs(words):
	buckets = defaultdict(list)
	graph = defaultdict(set)

	for word in words:
		for i in range(len(word)):
			bucket = '{}_{}'.format(word[:i], word[i + 1:])
			buckets[bucket].append(word)

	for buckets, mNeigh in buckets.items():
		for w1, w2 in product(mNeigh, repeat = 2): #take cartisian product of the two
			if (w1 != w2):
				graph[w1].add(w2)
				graph[w2].add(w1)

	return graph

def traverse(graph, startWord):
	seen = set()
	queue = deque([[startWord]])

	while(queue):
		path = queue.popleft()
		vertex = path[-1]
		yield vertex, path
#where n is the neighbour of the node
		for n in graph[vertex] - seen:
			seen.add(n)
			queue.append(path + [n])


if __name__ == '__main__':

	startWord = 'COLD'
	print('Start word:' + startWord)
	endWord = 'WARM'
	print('End word: ' + endWord)

	#calculation length of start/end word
	lengthOfStartWord = len(startWord)
	#print(lengthOfStartWord)
	wordGraph = buildGraphs(getWords(lengthOfStartWord,startWord,endWord))
	#pprint.pprint(wordGraph)
	
	for vertex, path in traverse(wordGraph, startWord):
		if (traverse(wordGraph, startWord)):
			if vertex == endWord:
				print('->'.join(path))

		else:
			print('Path does not exist!')
