import pickle

my_dict = {'1' : 'a', '2' : 'b'}
pickle_file=open('pocklefile.txt','wb')
pickle.dump(my_dict,pickle_file)

pickle_file=open('pocklefile.txt','rb')
new_dict=pickle.load(pickle_file)
print(new_dict)
pickle_file.close()

import json
mydict = ' { "1" : "a" , "2" : "b" , "3" : "c"} '
b = json.loads(mydict)
print(b)

with open("exa.json") as f:
    k=json.load(f)
print(k["4"])
print(json.dumps(k,indent=4))