import csv, random, string, sys, os
import markovify
import numpy.random
from collections import Counter

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from pattern.en import parsetree, PNPChunk, tag

import user_input_script
print user_input_script.main("I'm on top of the world.")


reload(sys)
sys.setdefaultencoding("utf-8")

def aliter_it(corpus): 
	return None

def getMarkov(corpus):
	text_model = markovify.Text(corp)
	for i in range(5):
		print i, text_model.make_sentence()
	for i in range(3):
		print i, text_model.make_short_sentence(140)
	return None

def getCounts(corpus, s): #here we want to get pos counts
	#let's get words per sentence, just for fun
	wds_per_sent = len(corpus)/s
	print "Average words per sentence:", wds_per_sent

	#get parts of speech
	count = dict()
	adjs, nouns = [], []
	vbs, advbs = [], []
	pronouns, cons = [], []
	tags = tag(corpus, tokenize=True, encoding='utf-8')
	for t in tags: 
		count[t[0]] = t[1]
		if t[1] == 'JJ': 
			adjs.append(t[0])
		elif t[1] == 'NN' or t[1] == 'NNP' or t[1] == 'NNS': 
			nouns.append(t[0])
		elif t[1] == 'VBD' or t[1] == 'VBG' or t[1] == 'VB' or t[1] == 'VBZ': 
			vbs.append(t[0])
		elif t[1] == 'RB': 
			advbs.append(t[0])
		elif t[1] == 'PRP' or t[1] == 'PRP$': 
			pronouns.append(t[0])
		elif t[1] == 'CC' or t[1] == 'DT': 
			cons.append(t[0])

	print random.choice(adjs), random.choice(nouns)
	print random.choice(adjs), random.choice(vbs), random.choice(nouns)

	start = random.randint(0, len(tags)-20)
	end = start + random.randint(7, 15)

	prescript = []
	for t in tags[start:end]: 
		if t[1] != '.' and t[1] != ":":
			prescript.append(t)

	print prescript

	pos = Counter(count.values())
#	print len(pos)
#	print pos.most_common()

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

	return

def main(corpus, user_shit): 
#	user = getUser(user_shit)
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
		print sample, type(sample)
		getCounts(corp, s)

		return 
		#ideally, this returns a binary of {RULE: 0, RULE:1}

	return None

corpus = 'C:/Users/skyet/OneDrive/CMU/76-429DigitalHumanities/James_Joyce_Is_Bonkers/test_corpus.txt'
user_shit = "You have to wake up. You have an exam in 10 minutes."
main(corpus, user_shit)
