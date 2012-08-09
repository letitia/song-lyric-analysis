#!/usr/bin/env python
# Letitia Lew 2011
# Reducer for Song lyrics by Genre project


from operator import itemgetter
import sys
import time

start = time.time()
mapping = 0

NUM_TOP_WORDS = 500

top_words_file = "top5000words.txt"
terms_file = "unique_terms.txt"
output_file = "output.txt"



# create array of top 5000 words
top_words = []
top_words.append("dummy 0th index")
top_f = open(top_words_file, 'r')
for line in top_f:
	line = line.strip()
	words = line.split(',')
	for word in words:
		top_words.append(word)
top_f.close()

# maps genres to a dictionary of words
genre2counts = {}
terms_f = open(terms_file, 'r')
for line in terms_f:
	term = line.strip()
	genre2counts[term] = {}
terms_f.close()

output_f = open(output_file, 'w')

for line in sys.stdin:
	line = line.strip()
	array = line.split('[')
	genre = array[0].strip()
	try:
		wordcounts = array[1]
		wordcounts = wordcounts.split(',')
		for wordcoloncount in wordcounts:
			wordcoloncount = wordcoloncount.strip(" ']")
			tuple = wordcoloncount.split(':')
			word = int(tuple[0])
			count = int(tuple[1])
			genre2counts[genre][word] = genre2counts[genre].get(word, 0) + count
	except ValueError, IndexError:
		pass


# write the results to STDOUT (standard output)
for genre, word_dict in genre2counts.items():
	sorted_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)
	array = []
	for word_index, count in sorted_dict[:NUM_TOP_WORDS]:
		array.append(top_words[word_index] + ":" + str(count))
	output_f.write(genre)
	output_f.write(" "+ ",".join(array) + "\n")

output_f.close()

# elapsed = time.time() - start + mapping
# print "time ", elapsed