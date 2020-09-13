import re, json
from stories import Story

def get_text(text):
    """get a list of prompts from textarea"""
    p = re.compile(r'(?!=\{)\w+[\s\w+]*(?=\})')
    return p.findall(text)

def append_data(title,text):

    with open("stories_db.json") as json_file:
        data = json.load(json_file)
      
    data.update({title: {
        "prompts": get_text(text),
        "template": text
    }})
    
    with open("stories_db.json",'w') as json_file: 
        json.dump(data, json_file, indent=4, separators=(',', ': '))
    

def load_data():
    tales = []
    with open("stories_db.json") as json_file:
        data = json.load(json_file)

    for key in data.keys():
        tales.append(Story(key,data[key]["prompts"],data[key]["template"]))

    return tales


        


    