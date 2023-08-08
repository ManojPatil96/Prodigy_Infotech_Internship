#!/usr/bin/env python
# coding: utf-8

# # Data Science Internship at Prodigy Infotech 2023

# # Name - Manoj Patil

# # Task-1: Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable.

# In[1]:


# Importing Required Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from warnings import filterwarnings
filterwarnings(action='ignore')


# In[8]:


df=pd.read_csv("DS_Prodigy_Task1_Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_5695140.csv")


# In[10]:


df.head()


# In[11]:


df.shape


# In[17]:


# Counting the occurrences of each region in the 'Region' column
gender_counts = df['Region'].value_counts()



# Plotting a bar chart using Seaborn's countplot
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='muted')



# Customize the plot

plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Distribution of Region')
plt.xticks(rotation=90)




# Add count numbers above each bar

for x, y in enumerate(gender_counts.values):
    plt.text(x, y, str(y), ha='center', va='bottom')
    
    
    
    
    
# Remove the top and right spines

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)



# Add a grid to the plot

plt.grid(axis='y', linestyle='--', alpha=0.5)



# Display the bar chart
plt.tight_layout()
plt.show()


# In[ ]:




