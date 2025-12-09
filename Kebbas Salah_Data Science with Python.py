#!/usr/bin/env python
# coding: utf-8

# In[30]:


pip install plotly


# In[31]:


pip install pandas


# In[39]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.express as px


# In[4]:


df = pd.read_csv("C:/Users/salah/Downloads/gapminder.csv")
df.head()


# In[9]:


df[df["life_exp"] > 75.320]


# In[10]:


df.isna().sum() 


# In[8]:


max = df["population"].max()
print(max)


# In[6]:


mean = df["gdp_cap"].mean()
print(mean)


# In[11]:


x=df["country"]
y=df["life_exp"]


plt.figure(figsize=(12, 6))
plt.bar(x, y, color="skyblue")

plt.xlabel("Country")
plt.ylabel("Life Expectancy")
plt.title("Life Expectancy by Country")

plt.xticks(rotation=90)   # rotate names so you can read them
plt.tight_layout()        # adjust spacing
plt.show()


# In[14]:


a=df["gdp_cap"]
b=df["life_exp"]

plt.figure(figsize=(8,5))
plt.scatter(a, b, color="green")

plt.xlabel("GDP per Capita")
plt.ylabel("Life Expectancy")
plt.title("Life Expectancy vs GDP per Capita")

plt.grid(True)  # optional, makes graph easier to read
plt.show()


# In[23]:


a = df["gdp_cap"]

fig = px.histogram(a, nbins=30, title="Histogram of GDP per Capita")
fig.show()


# In[24]:


df2 = pd.read_csv("C:/Users/salah/Downloads/Battery_dataset.csv")
df2.head()


# In[36]:


r=df2["SOH"]
t=df2["RUL"]
plt.figure(figsize=(8,5))
plt.scatter(r, t, color="green")

plt.xlabel("SOH")
plt.ylabel("RUL")

plt.grid(True)  
plt.show()


# In[43]:


fig2 = px.line(df2, x="RUL", y="SOH", title="Run Chart")
fig2.show()




# In[ ]:




