#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import sqlite3
import json
import numpy as np
import pymongo


# In[3]:


con=sqlite3.connect("examen.db")


# In[6]:


dfsqlite=pd.read_sql_query("SELECT * FROM en_venta", con)
dfsqlite=dfsqlite.set_index('id')
dfsqlite


# In[33]:


result = dfsqlite.to_json(orient="table")
parsed = json.loads(result)
aux=parsed.get('data')
datos = np.array(aux)


# In[36]:


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
    
for x in range(0,len(datos)):
    data=datos[x]
    try:
        destination = 'venta-bici'
        collection = client[MONGODB_DATABASE][destination]
        collection.insert_one(data)
        print ("Data saved at %s collection in %s database: %s" % (destination, MONGODB_DATABASE, data))
    except Exception as error:
        print ("Error saving data: %s" % str(error))


# In[ ]:
