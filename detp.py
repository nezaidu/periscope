import nltk
from nltk import pos_tag
from pattern.en import parse
def det(sentence):
	tokens=nltk.word_tokenize(sentence)
	return nltk.pos_tag(tokens)
def fun(sen):
	str1=parse(sen,tokenize=True,tags=True,chunks=False,encoding='utf-8')
	arr=det(sen)
	dic,dic2,dic3={},{},{}
	for el in arr:
		dic2[el[0]]=el[1]
	for key in str1.split(' '):
		one=key[0:key.find('/')]
		two=key[key.find('/')+1:]
		dic[one]=two
	for key in dic2:
		if key in dic:
			if dic2[key]!=dic[key]:
				dic3[key]=dic2[key]+','+dic[key]
			else:
				dic3[key]=dic2[key]
		else:
			dic3[key]=dic2[key]
	return dic3