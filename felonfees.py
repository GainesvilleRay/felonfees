#!/usr/bin/env python
# coding: utf-8

# In[1]:


#installed with pip
from pandas import pandas as pd
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#from email.message import EmailMessage

# built-in libraries
import csv
import datetime
#import os.path
import re
#import smtplib
#import sqlite3


# In[2]:


cols = ["casenum", "statute", "race", "gender", "total_owed", "total_dismissed",
    "total_due", "mandatory", "discretionary"]

df = pd.read_excel("Book3.xlsx",
                    usecols=[0, 1, 11, 12, 13, 15, 16, 17, 18],
                    names=cols,
                    encoding="ISO-8859-1")


# In[8]:


df = df.drop_duplicates(subset=['casenum'])
df.head(15)


# In[ ]:




