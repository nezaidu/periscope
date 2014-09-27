import argparse
from clean import clean
parser = argparse.ArgumentParser()
parser.add_argument("book", help="You must specify a list of books,separated by comma.All words from these books will be merged in one dictionary.Example:one.txt,two.txt")
args = parser.parse_args()
books=args.book.split(',')
words_you_know=[]

for book in books:
	a=[]
	for line in open(book):
		a+=line.strip().split(' ')
	words_you_know+=set(map(clean,a))
words_by_frequency=[line.strip() for line in open('gutenberg40000.txt')]


l=len(words_you_know)
inter=0.0
for i in range(len(words_by_frequency)):
	if words_by_frequency[i] in words_you_know:
		inter+=1
	if inter/l>0.60:
		f=open('dictionary.txt','w+')
		f.write('\n'.join(words_by_frequency[:i]))
		f.close()
		break