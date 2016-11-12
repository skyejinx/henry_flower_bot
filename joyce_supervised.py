import csv, random, string, sys, os
import markovify
import numpy.random
from collections import Counter

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from pattern.en import parsetree, PNPChunk, tag


reload(sys)
sys.setdefaultencoding("utf-8")
#exciting
#http://stackoverflow.com/questions/7443330/how-do-i-do-dependency-parsing-in-nltk

#just in case
def getMarkov(corpus):
	text_model = markovify.Text(corp)
	for i in range(5):
		print i, text_model.make_sentence()
	for i in range(3):
		print i, text_model.make_short_sentence(140)
	return None

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
	print wds_per_sent

	#get parts of speech
	count = dict()
	tags = tag(corpus, tokenize=True, encoding='utf-8')
	for t in tags: 
		count[t[0]] = t[1]

	#what are the pos that we care about? 
	#print count
	adjs, nouns = [], []
	count = dict()
	tags = tag(corpus, tokenize = True, encoding = 'utf-8')
	for tag in tags: 
		count[t[0]] = t[1]
		if t[1] == u'JJ': 
			adjs.append(t[0])
		elif t[1] == 'NN' or 'NPP' or 'NNPS' or 'NNP-LOC': 
			nouns.append(t[0])

	print random.choice(adjs), random.choice(nouns)
	pos = Counter(count.values())
	print "Parts of speech counts: ", pos.most_common()

	#we saved the number of sentences (s)
	#so we can count how many of each pos are in each sentence if we need to
	return

def getSentThings(sentences): #we need to use a list here
	print type(sentences)
	start = []
	for sent in sentences: 
		e = string.find(sent, ' ', 1)
		start.append(sent[0:e])
	print len(set(start))
	print(random.choice(start))
	#get the first word of each sentence
	#does this need to be a separate function? probably
	#we can also do average sentiment
	#and look at syllable patterns

	#it might be useful to plot those things here
	return

def getUser(user_input): 
	#This is what we want: 
	#https://foxtype.com/sentence-tree
	user_shit = set(user_input)
	count = dict()
	tags = tag(user_input, tokenize=True, encoding='utf-8')
	for t in tags: 
		count[t[0]] = t[1]

	pos = Counter(count.values())
	print len(pos)
	print pos.most_common()

	return None

def main(corpus, user_input): 
#	user = getUser(user_input)
	with open(corpus, 'r') as c: 
		#For now -- I think we have to do it this way for Rich Text Format reasons
		corp = c.readlines()
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
		print sample, type(sample)
		getCounts(corp, s)

		#ideally, this returns a binary of {RULE: 0, RULE:1}

	#if all these things happen 
	#we'll have binaries for each thing
	#doWeird(user_shit)

	return None

corpus = 'PATH TO CORPUS'
user_input = "You have to wake up. You have an exam in 10 minutes."
main(corpus, user_input)
