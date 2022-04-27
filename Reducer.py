#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
city = ""
current_city = ""
current_count = 0

for line in sys.stdin:
    city, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_city == city:
        current_count += count
    else:
        if current_city:
            print ' %s\t%d ' % (current_city, current_count)
        current_count = count
        current_city = city
if current_city == city:
    print ' %s\t%d ' % (current_city, current_count) 
        


# In[ ]:




