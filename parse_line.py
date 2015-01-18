from get_translation import get
from find import find
from detect_part import detect
from clean import clean


words=[line[0:-1].lower() for line in open('dictionary.txt','r')]
# words=['wanna','gonna']
words.sort()

def parse_line(sen,count):
	totranslate=[]
	k=[]
	k2={}
	dic={}
	for word in ' '.join(sen.split('\n')).split(' '):
		if find(words,clean(word))==0:
			k+=[clean(word)]
	if len(k)==0:
		return [sen,[]]
	else:
		par=detect(sen)
	for key in par:
		k2[clean(key)]=par[key]
	for key in k:
		if key in k2:
			dic[key]='{'+str(count)+'}'
			totranslate+=[(key,k2[key])]
			count+=1
	l=sen.split('\n')
	sen=' '.join(l)
	l=sen.split(' ')
	for i in range(len(l)):
		word=clean(l[i])
		if word in dic:
			l[i]+='<font color="#ff0000">'+dic[word]+'</font>'
	sen=' '.join(l)
	return [sen,totranslate]
