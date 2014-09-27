def clean(word):
	ind=word.find("n't")
	if ind!=-1:
		return clean(word[0:ind])
	l=list(map(chr, range(97, 123)))
	word=word.lower()
	ind1,ind2=0,len(word)+1
	for i in range(len(word)):
		if word[i] in l:
			ind1=i
			break
	for i in range(ind1,len(word)):
		if word[i] not in l:
			ind2=i
			break
	return word[ind1:ind2]