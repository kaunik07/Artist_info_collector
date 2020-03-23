import requests
import os
import json
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html

def artist_info(artist_name):
    url="https://musicbrainz.org/search?query="+artist_name+"&type=artist&method=indexed"
    # print(url)
    r=requests.get(url)
    artist={}
    biography={}
    social={}
    art=[]
    tree = html.fromstring(r.content)
    try:
        for i in range(1,5):
            chk_date=tree.xpath('//*[@id="content"]/table/tbody/tr['+str(i)+']/td[6]/text()')
            chk_name=tree.xpath('//*[@id="content"]/table/tbody/tr['+str(i)+']/td[1]/a/bdi/text()')
            chk_gender=tree.xpath('//*[@id="content"]/table/tbody/tr['+str(i)+']/td[4]/text()')
            # print(chk_name," ",chk_gender)
            # print(chk_gender)
            if(len(chk_date)!=0 or len(chk_gender)!=0):
                # print(i)
                if(chk_name[0]==artist_name):
                    # print("yes")
                    art.append(tree.xpath('//*[@id="content"]/table/tbody/tr['+str(i)+']/td[1]/a/@href'))
                    k=i
                    break
        artist_type=chk_type=tree.xpath('//*[@id="content"]/table/tbody/tr['+str(k)+']/td[3]/text()')
    except:
        print("Not found Artist Info")
        return artist
    # print(artist_type)
    # print(art[0][0])
    url="https://musicbrainz.org/"+art[0][0]
    r=requests.get(url)
    tree = html.fromstring(r.content)

    #social media links
    social_link = tree.xpath('//*[@id="sidebar"]/ul[1]//@href')
    social_link = social_link[:len(social_link)-1]
    social_name = tree.xpath('//*[@id="sidebar"]/ul[1]//@class')
    social_name = social_name[1:len(social_name)-1]
    for i in range(len(social_link)):
        social_name[i]=social_name[i][:-8]
        social[social_name[i]]=social_link[i]
    # print(social)

    #biography detials
    soup = BeautifulSoup(r.content,'lxml')
    biography["original_name"]=artist_name
    biography["type"]=chk_type[0]
    try:
        biography['dob']=soup.find(class_='begin-date').text[:4]
    except:
        print("No DOB")
    if(artist_type[0]=='Person'): 
        # print("Yes")
        original_name=tree.xpath('//*[@id="content"]/p[1]/text()')
        biography['original_name']=original_name[1]
        # print(original_name)
        if(len(original_name[1])==1):
            original_name = tree.xpath('//*[@id="content"]/p[1]/a/bdi/text()')
            biography['original_name']=original_name[0]
        elif(original_name[0]=='Showing official release groups by this artist. '):
            original_name=tree.xpath('//*[@id="content"]/div[4]/div/p[2]/b[1]')
            # print("yes")
            # print(original_name)
            biography['original_name']=''
        # print(original_name)
        biography['gender']=soup.find(class_='gender').text
        try:
            biography['dob']=soup.find(class_='begin-date').text[:10]
        except:
            print("No DOB")
    try:
        biography['area']=soup.find(class_='begin_area').text
    except:
        biography['area']=soup.find(class_='area').text
    # print(biography)
    artist['biography']=biography
    artist['social']=social
    return artist



