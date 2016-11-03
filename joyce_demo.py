import csv, random, sys, os
import markovify
import numpy.random

from nltk.tokenize import sent_tokenize
from pattern.en import parse

reload(sys)
sys.setdefaultencoding("utf-8")

def getCounts(corpus):
	counts = dict()
	#sample the corpus for 2,000 sentences
	#get infinitives
	#get conjunctions
	#get prepositions

	return counts

def getParts(user_shit): 
	sub = getSubject(user_shit)
	obj = getObject(user_shit)
	return (sub, obj)

def main(corpus): 
	with open(corpus, 'r') as c: 
		corp = c.read()
		print type(corp)
		corp = corp.replace('\n', ' ')
		corp = corp.replace('\xe2', ' ')
		corp = corp.replace('\x80', ' ')
		corp = corp.replace('\x94', ' ')
		sentences = sent_tokenize(corp)
		print len(sentences)
		sample = random.sample(sentences, 10)
		print sample
		return 
		text_model = markovify.Text(corp)
		for i in range(5):
			print i, text_model.make_sentence()
		for i in range(3):
			print i, text_model.make_short_sentence(140)

		random_sample_input = random.sample(k, 100)
		print random_sample_input



	return None

corpus = 'corpus.txt'
main(corpus)
