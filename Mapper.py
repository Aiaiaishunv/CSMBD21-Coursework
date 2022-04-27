#!/usr/bin/env python
# coding: utf-8

# In[18]:


import sys
import re
for line in sys.stdin:
    line = line.strip()
    cols = line.split(',')
    print ' %s\t%d ' % (cols[2], 1)
 


# In[ ]:




