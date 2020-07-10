import json

def parse_text_and_import_to_database(text):
    dictionary      = {}
    arr             = text.split('\n')
    arr[:]          = [x for x in arr if x]
    for i in range(len(arr)):
        arr[i]      = arr[i].split(' ', 1)
        arr[i][1]   = arr[i][1].strip()
        arr[i][0]   = arr[i][0].strip(',')

        if arr[i][0] in dictionary:
            dictionary[arr[i][0]].append(arr[i][1])
        else:
            dictionary[arr[i][0]] = [arr[i][1]]
    with open('data/database.json', 'w') as db:
        json.dump(dictionary, db)

    
