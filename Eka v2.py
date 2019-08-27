
# coding: utf-8

# In[2]:


#taanilan git: valmistelu.ipynb
#https://github.com/taanila/tilastoapu/blob/master/valmistelu.ipynb

import pandas as pd


# In[3]:


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


# In[4]:


df.count() #kaikkien sarakkeiden count


# In[6]:


df.isnull().sum() #kaikkien puuttuvien tietojen summa


# In[7]:


for var in df: #käydään kaikki muuttujat dataframen sisältä läpi
    print(var, pd.unique(df[var])) #haetaan jokaisesta sarakkeesta uniikkien tietojen lukumäärä


# In[9]:


df['sukup_teksti'] = df['sukup'].replace({1:'Mies', 2:'Nainen'}) #lisätään sarake ja muunnetaan sanakirjaa (dictionary) käyttäen 'sukup'-sarakkeen arvot
df.head(6)


# In[11]:


ika_bins = [18, 28, 38, 48, 58, 68]
df['ikäluokka'] = pd.cut(df['ikä'], ika_bins).astype(str) #luokitellaan ikä-tiedot valmiisiin koreihin
df.head(6)


# In[15]:


df['tyytyväisyys'] = df[['johto','työtov','työymp','palkkat','työteht']].mean(axis=1) #lasketaan keskiarvot valituista sarakkeista vaakasuuntaan
df[['nro','sukup','ikä','tyytyväisyys']].head(6)


# In[16]:


df['käyttö']= df[['työterv', 'lomaosa', 'kuntosa', 'hieroja']].count(axis=1)
df.head(6)


# In[17]:


df[4:6] #haetaan rivit 4-5


# In[18]:


df[df['palkka']>4000] #haetaan rivit yhden sarakkeen ehdon mukaan


# In[19]:


df[(df['sukup']==1) & (df['palkkat']<3)] #haetaan rivit ehdon mukaan: palkkaan tyytymättömät miehet


# In[20]:


df[df['käyttö']==0]


# In[24]:


df[['tyytyväisyys', 'käyttö']][df['käyttö']>=3] #valitaan sarakkeet ja haetaan rivit kolmannen sarakkeen ehdolla


# In[26]:


df[['palkka', 'palkkat']].sort_values(by='palkka').head(10) #järjestetään tulokset sarakkeen mukaan


# In[28]:


df[['palkka', 'palkkat']].sort_values(by='palkka', ascending=False).head(10)


# In[29]:


df.drop(['nro','ikä','palveluv','palkka'], axis=1).head()


# In[33]:


writer = pd.ExcelWriter('valmisteltu.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()

