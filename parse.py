# coding: utf-8
import sys
import pysrt
from get_translation import get
from find import find
from detp import fun
from clean import clean
words=[line[0:-1].lower() for line in open(sys.argv[3]+'.txt','r')]
words.sort()
subs = pysrt.open('final.srt',encoding='utf-8')
done=[]
arg1=int(sys.argv[1])
arg2=int(sys.argv[2])
for i in range(arg1 or 0,arg2 or len(subs)):
	print i,100*(float(i)/len(subs))
	sen=subs[i].text
	k=[]
	k2={}
	par=fun(sen)
	dic={}
	#print par
	for word in ' '.join(sen.split('\n')).split(' '):
		# print word,find(words,clean(word))
		if find(words,clean(word))==0:
		    k+=[clean(word)]
	for key in par:
		k2[clean(key)]=par[key]
	# print par
	for key in k:
		dic[key]=get(key,k2[key])
	l=sen.split('\n')
	sen=' '.join(l)
	l=sen.split(' ')
	for i in range(len(l)):
		word=clean(l[i])
		if word in dic:
			l[i]+='<font color="#ff0000">'+dic[word]+'</font>'
	sen=' '.join(l)
	done.append(sen)
for i in range(len(done)):
	subs[i].text=done[i]
subs.save('duck2.srt', encoding='utf-8')
f.close()
