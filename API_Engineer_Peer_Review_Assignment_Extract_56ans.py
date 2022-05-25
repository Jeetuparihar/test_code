#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/Images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 

# # Peer Review Assignment - Data Engineer - Extract API Data
# 

# Estimated time needed: **20** minutes
# 

# ## Objectives
# 
# In this part you will:
# 
# *   Collect exchange rate data using an API
# *   Store the data as a CSV
# 

# For this lab, we are going to be using Python and several Python libraries. Some of these libraries might be installed in your lab environment or in SN Labs. Others may need to be installed by you. The cells below will install these libraries when executed.
# 

# In[ ]:


#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y


# ## Imports
# 
# Import any additional libraries you may need here.
# 

# In[1]:


import requests
import pandas as pd


# ## Extract Data Using an API
# 

# Using ExchangeRate-API we will extract currency exchange rate data. Use the below steps to get the access key and to get the data.
# 
# 1.  Open the url : [https://exchangeratesapi.io/](https://exchangeratesapi.io/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01) and click on **Get Free API Key**.
# 2.  Subscribe for Free plan and Sign-in with the Google Account.
# 3.  Once the account is created you will be redirected to [https://apilayer.com](https://apilayer.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01) website.
# 4.  Now, click on the **user icon** and click **Account** as shown below:
# 
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/Images/account.png"/>
# 
# 3.  Scroll down and you will get the API Key section. Copy the API key and use in the url in Question 1.
# 

# ### Call the API
# 
# <b> Question 1</b> Using the `requests` library call the endpoint given above and save the text, remember the first few characters of the output:
# 

# In[10]:


# Write your code here
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=3NOGSjbv0KtzX9GoK8aqOzcQK9kTxy76"
req=requests.get(url)
req.json()


# ### Save as DataFrame
# 
# <b> Question 2</b>  Using the data gathered turn it into a `pandas` dataframe. The dataframe should have the Currency as the index and `Rate` as their columns. Make sure to drop unnecessary columns.
# 

# In[11]:


# Turn the data into a dataframe
dataframe=pd.DataFrame(req.json())
dataframe


# In[12]:


# Drop unnescessary columns
dataframe.drop(['success','timestamp','base','date'],axis=1)


# ### Load the Data
# 
# ##Using the dataframe save it as a CSV names `exchange_rates_1.csv`.
# 

# In[14]:


# Save the Dataframe
dataframe.to_csv(r'C:\Users\Jitendra Parihar\Python\exchange_rates_1.csv')


# Your CSV should be in this format with more currencies
# 
# |     | Rates      |
# | --- | ---------- |
# | AED | 4.398618   |
# | AFN | 92.917693  |
# | ALL | 123.099093 |
# | AMD | 621.935674 |
# | ANG | 2.149648   |
# 

# ## Authors
# 

# Ramesh Sannareddy, Joseph Santarcangelo and Azim Hirjani
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                              |
# | ----------------- | ------- | ----------------- | ----------------------------------------------- |
# | 2022-05-06        | 0.3     | Malika            | Updated instructions to get the API and the url |
# | 2021-04-15        | 0.2     | Malika            | Updated the lab from USD to EUR                 |
# | 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab              |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
