#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from matplotlib.font_manager import _rebuild
_rebuild()

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


# In[35]:


path = r'../YCdata/userloss.xls'
userloss = pd.read_excel(path)
userloss


# In[36]:


age = userloss['年龄']  #series 一维数组


# In[37]:


age.plot()  
plt.show()


# In[38]:


userloss.plot(x = "年龄",y = '在网时间',kind = 'scatter')
plt.show()


# In[39]:


from pandas.tool.plottin import radviz
radviz(userloss,'年龄')


# In[ ]:




