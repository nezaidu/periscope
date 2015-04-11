import urllib2
from pattern.en import lemma, singularize


def get(word, type, number_of_translations=4):
    types = type.split(',')
    if len(types) != 1:
        return get(word, types[0], 2) + '||' + get(word, types[1], 2)
    try:
        word = word.encode('ascii')
    except UnicodeDecodeError:
        return ''
    opener = urllib2.build_opener()
    opener.addheaders = [
    	('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
    	('referer', 'https://translate.google.com/'),
    ]
    res = opener.open(
        'https://translate.google.com/translate_a/single?client=t&sl=en&tl=ru&hl=ru&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&ssel=0&tsel=0&tk=519178|804751&q=' + word).read()
    tran = {}
    every_part = ''
    res = res.replace('adverb', 'adver_')
    parts_of_speech = [
        'adver_', 'verb', 'noun', 'conjunction', 'preposition', 'adjective']
    for part in parts_of_speech:
        if res.find(part) != -1:
            index = res.find(part) + len(part) + 4
            # print res[res.find(part):res.find(part)+len(part)]
            verge = res[index:].find(']') + len(res[0:index]) - 1
            tran[part] = (res[index:verge].split('","'))[
                0:number_of_translations]
            every_part += '||' + tran[part][0]
            tran[part] = '||'.join(tran[part])
        else:
            tran[part] = ''
    # print str(tran['verb']).decode('utf-8')
    if type[0] == 'J':
        return (tran['adjective'] or every_part).decode('utf-8')
    elif type[0] == 'V':
        if type != 'VB':
            return get(lemma(word), 'VB')
        return (tran['verb'] or every_part).decode('utf-8')
    elif type[0] == 'N':
        if type == 'NNP':
            t = get(word, 'NN')
            if t:
                return t
        if type == 'NNS':
            return(get(singularize(word), 'NN') or get(word, 'NN'))
        return (tran['noun'] or every_part).decode('utf-8')
    elif type[0] == 'R':
        return (tran['adver_'] or every_part).decode('utf-8')
    elif type == 'CC':
        return (tran['conjunction'] or every_part).decode('utf-8')
    else:
        return every_part.decode('utf-8')
