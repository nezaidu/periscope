import sys
import os
import urllib
import threading
from Queue import Queue
from get_translation import get
from det_part_of_speech import fun
from find import find
import pysrt
subs = pysrt.open('final.srt',encoding='utf-8')
done=[]
class DownloadThread(threading.Thread):
    def __init__(self, queue, destfolder):
        super(DownloadThread, self).__init__()
        self.queue = queue
        self.destfolder = destfolder
        self.daemon = True
    def run(self):

        while True:
            index = self.queue.get()
            try:
                self.translate_word(word)
            except Exception,e:
                print "   Error: %s"%e
            self.queue.task_done()

    def translate_word(self, index):
        print index,100*(float(index)/len(subs))
        sen=subs[index].text
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
def download(urls, destfolder, numthreads=100):
    words=[line.strip() for line in open('gutenberg40000.txt')][:1000]
    queue = Queue()
    for i in range(len(subs)):
        queue.put(i)
    for i in range(numthreads):
        t = DownloadThread(queue, destfolder)
        t.start()

    queue.join()
if __name__ == "__main__":
    download(sys.argv[1:], "/tmp")  