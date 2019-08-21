
# coding: utf-8

# In[2]:


#taanilan git: valmistelu.ipynb
#https://github.com/taanila/tilastoapu/blob/master/valmistelu.ipynb

import pandas as pd


# In[23]:


df = pd.read_excel('http://taanila.fi/data1.xlsx')
df.head() #5 ensimmäistä riviä


# In[9]:


df.tail() #5 viimeistä riviä, id antaa rivimäärän


# In[24]:


print( df.shape ) #antaa datarivien ja sarakkeiden määrän
print (df.columns) #antaa sarakkeiden nimet


# In[21]:


df.columns = ['nro', 's', 'i', 'p', 'k', 'pv', 'pk',
       'j', 'tto', 'ty', 'palkkat', 'tt', 'tte', 'l',
       'k', 'h'] #annetaan uusien sarakenimien lista (listat aina hakasulkeissa)
print (df.columns)


# In[31]:


df.rename(columns={'työymp':'työymp_id','perhe':'perhe_id'}, inplace=True) 
#käytetään sanakirjaa (aina aaltosulkeiden sisällä ja parit puolipistein erotettuna)
#inplace=True tallentaa muutokset dataobjektiin pysyvästi
df.head()


# In[32]:


df.describe() #tilastotiedot
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html


# In[34]:


df.corr() #kaikki 2-muuttujan korrelaatiokertoimet
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html

