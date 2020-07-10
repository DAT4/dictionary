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

def parse_text_and_import_to_database(text):
    dictionary      = {}
    arr             = text.split('\n')
    arr[:]          = [x for x in arr if x]
    for i in range(len(arr)):
        arr[i]      = arr[i].split(' ', 1)
        arr[i][1]   = arr[i][1].strip()

        if arr[i][0] in dictionary:
            dictionary[arr[i][0]].append(arr[i][1])
        else:
            dictionary[arr[i][0]] = [arr[i][1]]
    with open('data/database.json', 'w') as db:
        json.dump(dictionary, db)
