import requests
import json

f = open("config/r_k", "r")
def art_search(artist_id):
    # print(artist_id)
    m=[]
    for i in artist_id:
        url = "https://deezerdevs-deezer.p.rapidapi.com/artist/"+str(i)

        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': f.read()
            }
        response = requests.request("GET", url, headers=headers)
        # print(response)
        l=response.json()
        # print(l)
        k={}
        try:
            # print(f"{i} {l['name']}")
            k["id"]=l["id"]  
            k["name"]=l["name"]
            k["picture_small"]=l["picture_small"]
            k["picture_medium"]=l["picture_medium"]
            k["picture_big"]=l["picture_big"]
            k["albums"]=l["nb_album"]
        except:
            print("Not found Artist ID")
        m.append(k)
    return m