#!/usr/bin/env python
# coding: utf-8

#                         Exploratory Data Analysis of Bird Strikes between 2000 – 2011

# In[1]:


#Importing Numpy and Pandas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Loading Bird Strikes dataset
# bs= Bird Strikes 

bs = pd.read_excel('E:\Bird Strikes_Final.xlsx')


# In[3]:


bs.head(3) 


# In[4]:


#checking the shape of the dataset

bs.shape


# In[5]:


#describing the dataset

bs.describe()


# ## Data Preprocessing

# Check for Errors and Null Values
# 
# Replace Null Values with appropriate values
# 
# Drop down features that are incomplete and are not too relevant for analysis
# 
# Create new features that can would help to improve prediction

# In[6]:


#checking the null value in the dataset

bs_missing_values= bs.isnull().sum()
bs_missing_values


# In[7]:


bs_missing_value_percentage = (bs.isnull().sum()/ len(bs)*100)
bs_missing_value_percentage


# In[8]:


missing_values = pd.concat([bs_missing_values, bs_missing_value_percentage], axis=1,  keys=['Total','%'])
missing_values


# In[9]:


bs.columns


# In[10]:


#Drop Null Values
#By inserting the name of all the column which we want to drop 
#bs.dropna(subset=['Aircraft: Type', 'Airport: Name','Altitude bin','Wildlife: Number struck','Effect: Impact to flight','FlightDate','Aircraft: Airline/Operator','When: Phase of flight','Wildlife: Size','Pilot warned of birds or wildlife?','Feet above ground','Is Aircraft Large?'],inplace=True)
#or simpling inserting one column so that values from all the columm  will drop too.

bs.dropna(subset=['Aircraft: Type'],inplace=True)


# In[15]:


bs.isnull().sum()


# 'Remarks' may be dropped as it is highly incomplete or contains many null values

# In[16]:


bs.drop('Remarks', axis=1,inplace=True)


# 'Aircraft: Number of engines?'  may be dropped as it contains many null values as well as there is no need as per problem statements

# In[37]:


bs.drop('Aircraft: Number of engines?', axis=1, inplace =True)


# Filling missing Origin state by mode #mode the value that appears the most often in a data set and it can be used as a measure of central tendency

# In[67]:


bs['Origin State'] = bs['Origin State'].fillna(bs['Origin State'].mode()[0])


# In[68]:


bs.isnull().sum() #all null values removed


# In[70]:


bs.describe()


# In[71]:


bs.shape


# Now, Extract the data for visualization 

# In[72]:


bs.to_excel('E:\Bird Strikes Cleaned Data.xlsx')


# In[ ]:




