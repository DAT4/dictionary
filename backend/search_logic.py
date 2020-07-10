import re
import json
def search(word):
    word = word.upper()
    with open('data/database.json', 'r') as db:
        dictionary = json.load(db)
    try:
        return {'success':{word:dictionary[word]}}
    except:
        return {'error':{word:f'''The word "{' '.join([x for x in word])}" doesn't exist in dictionary'''}}, 404


def complex_search(word):
    word = word.upper()
    regex = ''
    for letter in word:
        if letter == '_':
            regex += '[a-zA-Z]'
        else:
            regex += letter
    with open('data/database.json', 'r') as db:
        dictionary = json.load(db)
    searchwords = []
    for i in dictionary:
        if re.fullmatch(regex,i):
            searchwords.append({i:dictionary[i]})
    if searchwords != []:
        return {'success':{word:searchwords}}
    else:
        return {'error':{word:f'''The word "{' '.join([x for x in word])}" doesn't exist in dictionary'''}}, 404

