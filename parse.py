# coding: utf-8
import sys
import pysrt
from get_translation import get
from find import find
from detp import fun
from clean import clean
from threading import Thread
from Queue import Queue
words=[line[0:-1].lower() for line in open('dictionary.txt','r')]
words.sort()
subs = pysrt.open('final.srt',encoding='utf-8')
done=[]
totranslate=[]
translated=[]
count=0
def parse(index):
	global count
	global totranslate
	# print index,100*(float(index)/len(subs))
	sen=subs[index].text
	k=[]
	k2={}
	par=fun(sen)
	dic={}
	for word in ' '.join(sen.split('\n')).split(' '):
		if find(words,clean(word))==0:
			k+=[clean(word)]
	for key in par:
		k2[clean(key)]=par[key]
	for key in k:
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
	subs[index].text=sen
for i in range(len(subs)):
	print i
	parse(i)
subs.save('duck2.srt', encoding='utf-8')
def worker():
	global totranslate
	global translated
	while True:
		index = q.get()
		print 'working with '+str(index)
		totranslate[index]=get(totranslate[index][0],totranslate[index][1])
		q.task_done()

q = Queue()
for i in range(30):
	 t = Thread(target=worker)
	 t.daemon = True
	 t.start()

for index in range(count):
	q.put(index)

q.join()   
# print totranslate
# print translated
import codecs
f=codecs.open('duck2.srt',mode='r+',encoding='utf-8')
s=f.read()
f.close()
f=codecs.open('duck5.srt',mode='w+',encoding='utf-8')
f.write(s.format(*totranslate))
f.close()