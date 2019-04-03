#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[1]:


pip install --upgrade ipython jupyter


# In[72]:


pip install plotly


# In[74]:


pip install dash==0.39.0  # The core dash backend


# In[75]:


pip install dash-daq==0.1.0 


# In[25]:


import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


plotly.tools.set_credentials_file(username='bytabo', api_key='xEQqTMh963kqLvWrTKbe')


# In[3]:


dat = pd.read_csv("data.csv", delimiter = ";")

dff = pd.DataFrame(dat.Betrag)
dgg = pd.DataFrame(dat.Kategorie)
dhh = pd.DataFrame(dat.Datum)
djj = pd.DataFrame(dat['offener Betrag'])


# In[7]:


trace = go.Table(
    header=dict(values=['Betrag','Kategorie', 'Datum', 'offener Betrag']),
    cells=dict(values=[dff, dgg, dhh, djj
                       ]))

data = [trace]

py.iplot(data, filename = 'basic_table')


# In[81]:


dffa = dff.Betrag.to_list()    

for i in range(len(dffa)):
    dffa[i] = dffa[i].replace(",", ".")
print(dffa)


dffb = [float(i) for i in dffa]
#dffb = np.array(dffa,dtype=float)

print(sum(dffb))


# In[92]:


betrag_versi = dat.Betrag.where(dat.Kategorie == "Firmenversicherung")
betrag_versi = betrag_versi.to_list()    

betrag_versi_cleaned = [x for x in betrag_versi if str(x) != 'nan']


for i in range(len(betrag_versi_cleaned)):
    betrag_versi_cleaned[i] = betrag_versi_cleaned[i].replace(",", ".")
#print(betrag_leasing_cleaned)

betrag_versi_cleaned = [float(i) for i in betrag_versi_cleaned]

print(sum(betrag_versi_cleaned))
b1= sum(betrag_versi_cleaned)

##############

betrag_leasing = dat.Betrag.where(dat.Kategorie == "Leasing für Geräte")
betrag_leasing = betrag_leasing.to_list()    

betrag_leasing_cleaned = [x for x in betrag_leasing if str(x) != 'nan']


for i in range(len(betrag_leasing_cleaned)):
    betrag_leasing_cleaned[i] = betrag_leasing_cleaned[i].replace(",", ".")
#print(betrag_leasing_cleaned)

betrag_leasing_cleaned = [float(i) for i in betrag_leasing_cleaned]

print(sum(betrag_leasing_cleaned))
b2 = sum(betrag_leasing_cleaned)


#############

betrag_haft = dat.Betrag.where(dat.Kategorie == "Betriebshaftpflicht")
betrag_haft = betrag_haft.to_list()    

betrag_haft_cleaned = [x for x in betrag_haft if str(x) != 'nan']


for i in range(len(betrag_haft_cleaned)):
    betrag_haft_cleaned[i] = betrag_haft_cleaned[i].replace(",", ".")
#print(betrag_leasing_cleaned)

betrag_haft_cleaned = [float(i) for i in betrag_haft_cleaned]

print(sum(betrag_haft_cleaned))
b3= sum(betrag_haft_cleaned)


# In[94]:


labels = ["Firmenversicherung","Leasing für Geräte","Betriebshaftpflicht"]
values = [b1,b2,b3]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')


# In[ ]:




