#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
from joblib import dump, load


# In[4]:


# traigo el modelo
model=load('elmodelo.joblib')


# In[5]:


st.title("Credit classifier")


# In[6]:


st.header('Indique las caracteristicas del cliente:')
credit = st.selectbox(
     'Credit Mix',['1', '2', '3'])
debt = st.slider('Outsatnding debt:', 0, 10000, 10) #hay que seleccionar el valor maximo y minimo

intr = st.slider('Interest rate', 0, 50, 1)

inq = st.slider('Number of credit inquiries', 1, 30, 1)

limit = st.slider('Changed credit limit', -15, 50, 1)


# In[7]:


pred=[credit,debt,intr,inq,limit]


# In[8]:


st.subheader('El cliente clasifica para el siguiente tipo de credito:')


# In[9]:


result = st.button('Run on image')
if result:
    st.write('Calculating results...')
    predict(model, pred)


# In[ ]:




