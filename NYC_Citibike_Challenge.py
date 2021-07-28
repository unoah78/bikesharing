#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


# 1. Create a DataFrame for the 201908-citibike-tripdata data. 
tripdata_df = pd.read_csv("201908-citibike-tripdata.csv")
tripdata_df


# In[5]:


# 2. Check the datatypes of your columns. 
tripdata_df.dtypes


# In[6]:


# 3. Convert the 'tripduration' column to datetime datatype.
tripdata_df['tripduration'] = pd.to_datetime(tripdata_df['tripduration'], unit='s')


# In[7]:


# 4. Check the datatypes of your columns. 
tripdata_df.dtypes


# In[8]:


tripdata_df.head()


# In[9]:


# 5. Export the Dataframe as a new CSV file without the index.
tripdata_df.to_csv("citibike_data.csv", index=False)


# In[ ]:




