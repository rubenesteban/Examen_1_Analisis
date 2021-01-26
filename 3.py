#!/usr/bin/env python
# coding: utf-8

# In[1]:


from facebook_scraper import get_posts
import json
import pymongo


# In[2]:


URI_CONNECTION = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'bicicletas'

try:
    client = pymongo.MongoClient(URI_CONNECTION)
    client.server_info()
    print ('OK -- Connected to MongoDB at server %s' % ('localhost'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB: %s' % error)

for post in get_posts('idealista',pages=10): 
    try:
        destination = 'venta-bici'
        collection = client[MONGODB_DATABASE][destination]
        collection.insert(post)
        print ("Data saved at %s collection in %s database: %s\n\n" % (destination, MONGODB_DATABASE, post))
    except Exception as error:
        print ("Error saving data: %s" % str(error))


# In[ ]:
