#!/usr/bin/env python
# coding: utf-8

# # analise top 200 youtubers

# In[3]:


# BAIXAR BIBLIOTECAS: PANDAS, PLOTLY.

get_ipython().system('pip install pandas')

get_ipython().system('pip install plotly.express ')


# In[4]:


# IMPORTAR BIBLIOTECA PANDAS, PLOTLY.

import pandas as pd

import plotly.express as px


# In[5]:


# ENTRADA DE DADOS:

tabela = pd.read_csv("top_200_youtubers.csv")


# LIMPEZA DE TABELA
tabela = tabela.drop("Youtube Link",axis=1)

tabela = tabela.drop("More topics",axis=1)



# DELETANDO LINHAS QUE TENHA RESPOSTAS NA
tabela = tabela.dropna(how="all", axis=1)


# CONVERTENDO DADO TIPO OBJECT PARA FLOAT 64
#tabela["Country"] = pd.to_numeric(tabela["Country"], errors="coerce")
#tabela["Channel Name"] = pd.to_numeric(tabela["Channel Name"], errors="coerce")
#tabela["Category"] = pd.to_numeric(tabela["Category"], errors="coerce")
#tabela["Main Video Category"] = pd.to_numeric(tabela["Main Video Category"], errors="coerce")
#tabela["username"] = pd.to_numeric(tabela["username"], errors="username")
#tabela["Main topic"] = pd.to_numeric(tabela["Main topic"], errors="coerce")




# In[50]:


# observar tabela:

display(tabela)

print(tabela.info())

# APRESENTAR PORCENTAGEM DOS PAISES COM MAIS CANAIS FAMOSO
print(tabela["Country"].value_counts(normalize=True).map("{:.1%}".format))


# In[6]:


grafico = px.histogram(tabela, x="Likes", color="Country")


# In[7]:


grafico.show()


# Brasil tem uma taxa de visualizações de 10 bilhões a mais que estados unidos.
# 
# EUA apesar de não ter a maiox taxa de viws tem a maior taxa de likes comparando ao brasil.
# 
# apesar de ter menos inscrito que os estados unidos brasil tem taxa de viws maior.

# In[ ]:




