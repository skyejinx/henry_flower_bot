"""
NOTES:

--OBJECTS AND HIERARCHY:

Pattern breaks text as follows:  
Text -> Sentence -> Chunk -> > Word 

Each object functions as a list of the next object and can be iterated as such. It is
important to note that each object is not *actually* a list.


--MULTIPLE SUBJECTS, VERBS AND OBJECTS:

Does not detect multiple subjects well., verbs and objects.
As example, Tom and Jerry ate cheese has one subject NP, Tom and Jerry,
and one simple subject Jerry. 
"""


from pattern.en import parse
from pattern.en import parsetree
from pattern.en import Sentence
import random


input = 'The wonderous wizard sternly summoned the magic fox.'
# parse input into Text object
text = parsetree(input, relations = True, lemmata=True)

for sentence in text:
    # print subject(s)
    print '\nSubject(s)'
    for chunk in sentence.subjects:
        # prints the NP (noun phrase) chunks
        print chunk.string
        # prints the simple subjects a.k.a the "head" noun/pronouns
        print chunk.head.string
    
    # print verb(s)
    print '\nVerb(s)'
    for chunk in sentence.verbs:
        # prints the VP (verb phrase) chunks
        print chunk.string
        # prints the simple verbs a.k.a the "head" verbs
        print chunk.head.string

    # print object(s)
    print '\nObject(s)'
    for chunk in sentence.objects:
        # prints the NP (noun phrase) chunks
        print chunk.string
        # prints the simple objects a.k.a the "head" objects
        print chunk.head.string


#  pre: takes a pattern sentence object
# post: returns a simple subject (random if multiple)
def getSubject(sentence):
    if sentence.subjects:
        return random.choice(sentence.subjects).head.string
    else:
        return None

#  pre: takes a pattern sentence object
# post: returns a simple verb (random if multiple)
def getVerb(sentence):
    if sentence.verbs:
        return random.choice(sentence.verbs).head.string
    else:
        return None

#  pre: takes a pattern sentence object
# post: returns a simple object (random if multiple)
def getObject(sentence):
    if sentence.objects:
        return random.choice(sentence.objects).head.string
    else:
        return None


print '\nPrint function outputs...'
print getSubject(text[0])
print getVerb(text[0])
print getObject(text[0])


