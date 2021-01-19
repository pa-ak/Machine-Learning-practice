#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas
data = pandas.read_csv('C:\\Users\\User\\Documents\\AI\\ML course\\titanic.csv', index_col='PassengerId')


# In[10]:


data[:10]


# In[11]:


data.head()


# In[12]:


data['Pclass']


# In[13]:


data[:]


# In[14]:


data['Pclass'].value_counts()


# In[20]:


import pandas as pd
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df


# In[34]:


data['Sex'].value_counts()


# In[212]:


data['Survived'].value_counts()


# In[215]:


342/891


# 

# In[213]:


data['Pclass'].value_counts()


# In[214]:


216/891


# In[38]:


data['Age'].mean()


# In[39]:


data['Age'].median()


# In[40]:


data['Age'].value_counts()


# In[42]:


data['SibSp'].corrwith('Parch', axis=0, drop=False, method='pearson')


# In[44]:


data['SibSp'].corr(data['Parch'], method='pearson', min_periods=None)


# In[45]:


data[:]


# In[46]:


data['Name']


# In[47]:


data['Name'].sort_values()


# In[154]:


Gender = data[['Name', 'Sex']].to_numpy()
Gender


# In[210]:


Ladies_Names = []
count_ladies_names = 0

for name in Gender:
    if name[-1] == 'female':
        Ladies_Names.append(name[0].split())
        count_ladies_names += 1

count_ladies_names


# In[211]:


Ladies_Names_2 = []

for person in Ladies_Names:
    Ladies_Names_2.append(person[1:])
    


# In[209]:


Ladies_First_Names = []
count_ladies = 0

#check for special cases where the name is in () 
for lad_name in Ladies_Names_2:
    for ln in lad_name:
        if ln.startswith('("Mrs.'):
            Ladies_First_Names.append(lad_name[1])
            count_ladies += 1
            break
        elif ln.startswith('('):
            Ladies_First_Names.append(ln[1:])
            count_ladies += 1
            break
    # for all other cases just take the first word after Mrs. or Miss.       
    if not lad_name[-1].endswith(')'):    
        if lad_name[1].startswith('Miss') or lad_name[1].startswith('Mrs'): 
            Ladies_First_Names.append(lad_name[2])
            count_ladies += 1
        else:    
            Ladies_First_Names.append(lad_name[1])
            count_ladies += 1
        


LFN = pd.DataFrame(Ladies_First_Names, columns = ['First Name'])

count_ladies
        
Ladies_First_Names


# In[207]:


Final_Names = pd.DataFrame(Ladies_First_Names, columns = ['First Names'])
Final_Names


# In[208]:


Final_Names['First Names'].value_counts()


# In[ ]:




