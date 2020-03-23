import os
import json
import simplejson
from artist_social_media import artist_info
from artist_search import art_search

print("Artists ID")
st=input()
T=[]
NT=[]

for i in art_search(st.split()):
    try:
        print(f'{i["id"]}  {i["name"]}')
        n={}
        if(len(artist_info(i['name']))!=0):
            n["name"]=i["name"]
            n.update(artist_info(i['name']))
            n["picture_small"]=i["picture_small"]
            n["picture_medium"]=i["picture_medium"]
            n["picture_big"]=i["picture_big"]
            T.append(n)
        else:
            NT.append(i['id'])
            # print("Nope")    
    except KeyboardInterrupt:
        break 
    except:
        continue
json = json.dumps(T)
f = open("artist_details.json","w")
f.write(json)
f.close()
ff= open('not_found.txt', 'w')
simplejson.dump(NT, ff)
ff.close()
print ("Completed!!!!")