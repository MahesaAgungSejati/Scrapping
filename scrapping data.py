#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# Making a GET request
r = requests.get('https://proxyway.com/reviews')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)


# In[2]:


import requests

# Making a GET request
r = requests.get('https://proxyway.com/reviews')

# print request object
print(r.url)

# print status code
print(r.status_code)


# In[3]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://proxyway.com/reviews')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)

# Getting the name of parent tag
print(soup.title.parent.name)

# use the child attribute to get
# the name of the child tag


# In[6]:


import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")


# In[14]:


import csv
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

data = []

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")
        data.append({
            'Page Number': f'Page {page}',
            'Title Number': f'Title {i+1}',
            'Title Name': title.text
        })

# Menyimpan data ke dalam file CSV
filename = 'proxywaydata.csv'
fieldnames = ['Page Number', 'Title Number', 'Title Name']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data telah disimpan ke dalam file", filename)


# In[ ]:




