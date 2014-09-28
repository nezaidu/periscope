import sys
import pysrt
from threading import Thread
from Queue import Queue
import argparse
import codecs
from shutil import copyfile
from parse_line import *
done=[]
totranslate=[]
def parse_file(f):
	global totranslate
	f+='.srt'
	subs = pysrt.open(f,encoding='utf-8')
	copyfile(f,'OLD'+f)
	for i in range(len(subs)):
		print i
		sen=subs[i].text
		parsed_line=parse_line(sen,len(totranslate))
		subs[i].text=parsed_line[0]
		totranslate+=parsed_line[1]
	subs.save(f, encoding='utf-8')
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

	for index in range(len(totranslate)):
		q.put(index)

	q.join()   
	fl=codecs.open(f,mode='r+',encoding='utf-8')
	s=fl.read()
	fl.close()
	fl=codecs.open(f,mode='w+',encoding='utf-8')
	fl.truncate()
	fl.write(s.format(*totranslate))
	fl.close()
#dispensed

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['file','dir'],help='You can parse file or entire directory.')
parser.add_argument('destination',help='Destination to file/directory.')
args = parser.parse_args()
if args.mode=='file':
	parse_file(args.destination)