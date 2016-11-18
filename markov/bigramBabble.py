import random
import string

nonword = "\n" # new line character

def strip_punc(word):
  return ''.join(ch for ch in word if ch not in string.punctuation)

def parse_file(filename):
  w1 = nonword
  w2 = nonword
  table = dict()
  with open(filename, 'r') as f:
    contents = f.read()
  words = contents.split()
  for word in words:
    word = strip_punc(word)
    table.setdefault( (w1, w2), []).append(word)
    w1, w2 = w2, word
  return table

def babble(table, babble_length):
  w1 = nonword
  w2 = nonword
  result = ""
  for i in xrange(babble_length):
    new_word = random.choice(table[w1,w2])
    result += " " + new_word
    w1, w2 = w2, new_word
  return result


def main(filename):
  table = parse_file(filename)
  output = babble(table, 100)
  return output


print main("corpus.txt")