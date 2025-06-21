#!/usr/bin/env python
# coding: utf-8

# ## **Data Analysis Python Project - Blinkit Analysis**

# #### **Import Libraries**

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("D:/PROJECTS/Python Projects/blinkit_data.csv")


# In[6]:


df.head(20)


# In[18]:


df.tail(10)


# #### **Size of Data**

# In[7]:


print("Size of Data:",df.shape)


# #### **Fiels Info**

# In[8]:


df.columns


# #### **Data Types**

# In[9]:


df.dtypes


# #### **Data Cleaning**

# In[10]:


print(df['Item Fat Content'].unique())


# In[11]:


df['Item Fat Content'] = df['Item Fat Content'].replace({ 'LF': 'Low Fat',
                                                          'low fat': 'Low Fat',
                                                          'reg': 'Regular'
                                                        })


# In[12]:


print(df['Item Fat Content'].unique())


# ### **Business Requirements**

# ### **KPI's Requirement**

# In[13]:


#Total Sales
total_sales = df['Sales'].sum()

#Average Sales
avg_sales = df['Sales'].mean()

#No of Items Sold
no_of_item_sold = df['Sales'].count()

#Average Ratings
avg_ratings = df['Rating'].mean()

#Display
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Average Sales: ${avg_sales:,.0f}")
print(f"No of Item Sold: {no_of_item_sold:,.0f}")
print(f"Average Ratings: {avg_ratings:,.0f}")


# ### **Charts Requirements**
# 

# #### **Total Sales by Fat Content**

# In[14]:


sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

plt.pie(sales_by_fat, labels = sales_by_fat.index,
                     autopct = '%.0f%%',
                    startangle = 90)

plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()


# #### **Total Sales by Item Type**

# In[15]:


sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)

plt.xticks(rotation=-90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f'{bar.get_height():,.1f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
    


# #### **Fat Content By Outlet for Total Sales**

# In[47]:


grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped [['Regular', 'Low Fat']]

ax = grouped.plot(kind='bar', figsize=(8,5), title='Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Loaction Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()


# #### **Total Sales by Outlet Establishment**

# In[18]:


sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x,y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x,y,f'{y:,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()


# #### **Sales by Outlet Size**

# In[21]:


sales_by_size = df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(4, 4))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()


# #### **Sales by Outlet Location**

# In[23]:


sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales', ascending=False)

plt.figure(figsize=(8,3))  #smaller height, enough width
ax=sns.barplot(x='Sales', y='Outlet Location Type', data=sales_by_location)

plt.title('Total Sales by Outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')

plt.tight_layout()
plt.show()


# In[ ]:




