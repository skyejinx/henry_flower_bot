import random
import string

#strips punctuation
def strip_punc(word):
    return ''.join(ch for ch in word if ch not in string.punctuation)

def parse_file(filename):
    table = dict()
    with open(filename, 'r') as f:
        contents = f.read()
    words = contents.lower().split()
    
    for i in xrange(1, len(words)):
        curr_word = strip_punc(words[i])
        prev_word = strip_punc(words[i-1])
        table.setdefault(prev_word, []).append(curr_word)
    return table


def babble(table, babble_length):
    curr_word = random.choice(table.keys())
    result = curr_word
    for i in xrange(babble_length):
        new_word = random.choice(table[curr_word])
        result += " " + new_word
        curr_word = new_word
    return result


def main(filename):
    table = parse_file(filename)
    output = babble(table, 100)
    return output


print main("corpus.txt")
