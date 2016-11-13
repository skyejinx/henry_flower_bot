import csv, random, string, sys, os
import markovify
import numpy.random
from collections import Counter

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from pattern.en import parse, parsetree, PNPChunk
from pattern.en import tag, Sentence
import random


from PyDictionary import PyDictionary
dictionary=PyDictionary()

#import user_pattern -- Steve's script that handles the user

reload(sys)
sys.setdefaultencoding("utf-8")
#exciting
#http://stackoverflow.com/questions/7443330/how-do-i-do-dependency-parsing-in-nltk

def images(corpus): 
	colors = []
	vision = []
	return None

def alliterIt(corpus): 
	#tokenize to words
	#check [0] for each word
	#if [0] repeated, store the max
	#return max
	return None

def getWeird(corpus): 
	#do sentences start with lowercase letters?
	if images(corpus): 
		pass
	if alliterIt(corpus):
		pass
	#alliteration
	#rhymes? 
	return 

def getCounts(corpus, s): #here we want to get pos counts
	#let's get words per sentence, just for fun
	wds_per_sent = len(corpus)/s
	print "Avg words per sentence:", wds_per_sent

	#get parts of speech
	adjs, nouns = [], []
	count = dict()
	tags = tag(corpus, tokenize=True, encoding='utf-8')
	for t in tags: 
		count[t[0]] = t[1]
		if t[1] == u'JJ': 
			adjs.append(t[0])
		elif t[1] == 'NN' or 'NNP' or 'NNPS' or 'NNP-LOC': 
			nouns.append(t[0])

	print "Sample tags: ", tags[0], tags[0][1]

	print "Example Joyce: ", random.choice(adjs), random.choice(nouns)

	pos = Counter(count.values())
#	print len(pos)
	print "Parts of speech counts:", pos.most_common()

	#we saved the number of sentences (s)
	#so we can count how many of each pos are in each sentence if we need to
	return

def getUser(user_shit): 
	#we'll import from Steve's script when it's ready
	count = dict()
	tags = tag(user_shit, tokenize=True, encoding='utf-8')
	for t in tags: 
		count[t[0]] = t[1]
	print tags

	pos = Counter(count.values())
	print len(pos)
	print pos.most_common()

	return None

def main(user_shit): 
	user = getUser(user_shit)
	with open(corpus, 'r') as c: 
		corp = c.readlines()
		print type(corp)
		for i in xrange(0, len(corp)): 
			corp[i] = corp[i].replace('\n', '')
			corp[i] = corp[i].replace('\xe2', '')
			corp[i] = corp[i].replace('\xa3', '')
			corp[i] = corp[i].replace('\x80', '')
			corp[i] = corp[i].replace('\x94', '')
			
		corp = string.join(corp)
		sentences = sent_tokenize(corp)
		print len(sentences)
		getSentThings(sentences)

		s = 10 #number of sentences, this will come up later
		sample = string.join(random.sample(sentences, s))
#		print sample, type(sample)
		getCounts(corp, s)

		#ideally, this returns a binary of {RULE: 0, RULE:1}
	return None

#corpus = 'C:/Users/skyet/OneDrive/CMU/76-429DigitalHumanities/James_Joyce_Is_Bonkers/test_corpus.txt'
corpus = "PATH TO CORPUS"
user_shit = "You have to wake up. You have an exam in 10 minutes."
#main(corpus, user_shit)

main(user_shit)