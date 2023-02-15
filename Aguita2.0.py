#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install plyer


# In[ ]:


import time
import plyer
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Último momento!!!",
            message = "A tomar agua, pasaron 5 hs",
            timeout = 10
        )
        time.sleep(18000)


# In[ ]:




