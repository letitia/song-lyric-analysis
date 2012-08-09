#!/usr/bin/python
# Letitia Lew 2011

"""
The most frequently used words in song lyrics by genre.

Sources:
- The Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.
analyze_test_set.py		Copyright 2010, Thierry Bertin-Mahieux

- musiXmatch dataset, the official lyrics collection for the Million Song Dataset, available at: http://labrosa.ee.columbia.edu/millionsong/musixmatch

"""

import sys
import re
import time
import sqlite3


# Simple utility function to make sure a string is proper to be used in a SQLite query
def encode_string(s):
    return "'"+s.replace("'","''")+"'"


start = time.time()

top_words_file = "top5000words.txt"
track_db_file = "track_metadata.db"
artist_term_db_file = "artist_term.db"


stoplist = ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','get','got','go','let','say','make','want','feel','give','need','gonna','wanna','take','would','could','still','way','see','never','know','put','come','time','life','have','has','had','do','does','did','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','one','once','right','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','like','s','t','well','can','will','just','don','should','man','que','un','now','us','yeah','back','ich','du','und','da','tu','wo','oh','de','la','ya','ca','ai','d','m','n','y','w','e']

genres = ["hyphy",
"east coast rap",
"east coast hip hop",
"west coast rap",
"west coast hip hop",
"heavy metal",
"pop",
"70s",
"80s"
]

def main(argv):
	
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
	
	
	# open connections
	conn_track = sqlite3.connect(track_db_file)
	conn_at = sqlite3.connect(artist_term_db_file)


	line = sys.stdin.readline()
	try:
		while line:
			line = line.strip()
			array = line.split(',')
			track_id = array[0]
			q = "SELECT songs.artist_id FROM songs WHERE track_id = '" + track_id + "'"
			artist_result = conn_track.execute(q)
			artist_id = artist_result.fetchone()[0]
			
			q2 = "SELECT artist_term.term FROM artist_term WHERE artist_term.artist_id = '" + artist_id + "'"
			terms_result = conn_at.execute(q2)
			terms = terms_result.fetchall()
			
			# emit genre, list of wordcounts
			
			for tuple in terms:
				term = tuple[0]
				tokens = []
				wordcounts = array[2:len(array)]
				for wc in wordcounts:
					wctuple = wc.split(':')
					word = top_words[int(wctuple[0])]
					if word not in stoplist:
						token = wctuple[0] + ":" + wctuple[1]
						tokens.append(token)
				print term, tokens
			line = sys.stdin.readline()		
	except "end of file":	
		conn_at.close()
		conn_track.close()
		return None

#elapsed = (time.time() - start)
#print "time[", elapsed

if __name__ == "__main__":
	main(sys.argv)

