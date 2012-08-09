#!/usr/bin/python


stoplist = ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','get','got','go','let','say','make','want','feel','give','need','gonna','wanna','take','would','could','still','way','see','never','know','put','come','time','life','have','has','had','do','does','did','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','one','once','right','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','like','s','t','well','can','will','just','don','should','man','que','un','now','us','yeah','back','ich','du','und','da','tu','wo','oh','de','la','ya','ca','ai','d','m','n','y','w','e']

filtered = []

f = open('top5000words.txt')
line = f.readline()
f.close()

line = line.strip()
array = line.split(',')

for word in array:
	if word not in stoplist:
		filtered.append(word)


for word in filtered:
	print word
