import csv, random, os
import markovify

def main(corpus): 
	with open(corpus, 'r') as c: 
		corp = c.read()
		text_model = markovify.Text(corp)
		for i in range(5):
			print i, text_model.make_sentence()
		for i in range(3):
			print i, text_model.make_short_sentence(140)

	return None

corpus = PATH_TO_CORPUS
main(corpus)
