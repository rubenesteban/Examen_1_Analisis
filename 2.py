#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import pymongo


# In[2]:


def find_2nd(string, substring):
    return string.find(substring, string.find(substring)+1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))

response = requests.get("https://listado.mercadolibre.com.ec/bicicletas-ciclismo")
soup=BeautifulSoup(response.content, "lxml")

Marca=[]
Detail=[]
Price=[]
Tipo=[]


# In[3]:


post_marca= soup.find_all("span", class_= "_2tW1I")
post_detail= soup.find_all("span", class_= "_2TVI3")
post_price= soup.find_all("span", class_= "_89yzn")
post_tipo= soup.find_all("span", class_="tjgMj")

for element in post_marca:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Title.append(limpio.strip())
for element in post_detail:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Detail.append(limpio.strip())
for element in post_price:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Price.append(limpio.strip())
for element in post_tipo:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Location.append(limpio.strip())


# In[4]:


aux=[]
for x in range(0,len(Marca)):
    data={'marca':Marca[x],'detail':Detail[x],'tipo':Tipo[x],'price':Price[x]}
    aux.append(data)

URI_CONNECTION = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'bicicletas'

try:
    client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=100000, maxPoolSize=10)
    client.server_info()
    print ('OK -- Connected to MongoDB at server %s' % ('localhost'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB: %s' % error)
    
for x in range(0,len(aux)):
    data=aux[x]
    try:
        destination = 'venta-bici'
        collection = client[MONGODB_DATABASE][destination]
        collection.insert_one(data)
        print ("Data saved at %s collection in %s database: %s" % (destination, MONGODB_DATABASE, data))
    except Exception as error:
        print ("Error saving data: %s" % str(error))
