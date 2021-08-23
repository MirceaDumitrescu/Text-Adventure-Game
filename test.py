import json


#Load data from json file, into a dict
def read():
        return json.load(open('data.json'))
#Write into json file, as a dict
def write():
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

data = {
    'demo': {
        1: 'one',
        2: 'two',
        'demo 1': {
            3: 'three',
            4: 'four'
        }
    }
}


try:
    print(read())
    
except:
    write()