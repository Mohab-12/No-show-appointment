#!/usr/bin/env python
# coding: utf-8

# Here is an investigation about patients dataset who does/doesnt show up on their appointment.
# My first question is investigation is who is more inclined to to decline their appointment(male/female)? Have they recieved an sms? 
# My second question is Which neighbourhood is has more patients, and which percentage is more male or female?! and which disease is most common and also filtered with gender?!

# Import libraries need for the project

# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# implement a function to as k the user if he wants to investigate the dataset

# In[29]:


def wish ():
    x=input("Do you want to invesitage a dataset ")
    if x=='yes':
        print("Let's go ")
    if x=="no":
        print("Thank you for your time")
    return x

wish()  


# Dataset exploration

# In[32]:


#Dataset exploration
df=pd.read_csv("noshowappointments-kagglev2-may-2016.csv")
df.head()


# Check type of columns

# In[31]:


#Check type of columns
df.dtypes


# Check the Nan values

# In[33]:


#Check the Nan values
df.isnull().values.any()


# check duplicates

# In[34]:


#check duplicates
df.duplicated()


# checking the number of patients that have arrived, and vise versa

# In[35]:


#checking the number of patients that have arrived, and vise versa
df["No-show"].value_counts()


# checking the number of females/males

# In[36]:


#checking the number of females/males
df["Gender"].value_counts()


# Exploring which gender has more scholarship

# In[37]:


#Exploring which gender has more scholarship
sns.countplot(x='Gender',data=df,hue='Scholarship')
plt.show()


# Numbre of people filtered by gender who didnt show/show in the appointment

# In[38]:


#Numbre of people filtered by gender who didnt show/show in the appointment
sns.countplot(x='No-show',data=df,hue='Gender')
plt.show()


# Number of people filtered by gender  according to the neighbourhood. It also allows us to know which neighbourhood has moere patients

# In[39]:


#Number of people filtered by gender  according to the neighbourhood. It also allows us to know which neighbourhood has moere patients
plt.figure(figsize=(15,5))
sns.countplot(x='Neighbourhood',data=df,hue='Gender')
plt.xticks(rotation=90)
plt.title("Neighoburhood's patient density")
plt.show()


# Number of people who 
#     recieved/not recieved SMS filtered by gender

# In[40]:


#Number of people who recieved/not recieved SMS filtered by gender
sns.countplot(x='SMS_received',data=df, hue='Gender')
plt.xticks(rotation=90)
plt.show()


# Number of patients per day filtered by gender

# In[41]:


#Number of patients per day filtered by gender
plt.figure(figsize=(10,5))
df['AppointmentDay']=pd.to_datetime(df['AppointmentDay'])
sns.barplot(x="AppointmentDay",y='PatientId', data=df,hue="Gender") 
plt.xticks(rotation=90)
plt.show()                                               


# check the patients health in terms of the following diseaes, and filtering according to gender.

# In[42]:


#check the patients health in terms of the following diseaes, and filtering according to gender.
fig,ax=plt.subplots(1,4,figsize=(22,4))
fig.suptitle('Diseases among patients')
sns.countplot(ax=ax[0], x='Hipertension',data=df, hue='Gender')
sns.countplot(ax=ax[1], x='Diabetes',data=df, hue='Gender')
sns.countplot(ax=ax[2], x='Alcoholism',data=df, hue='Gender')
sns.countplot(ax=ax[3], x='Handcap',data=df, hue='Gender')


# Counting the number of handicap patients

# In[43]:


#Counting the number of handicap patients
df['Handcap'].value_counts()


# counting the diabetes patients

# In[44]:


#Counting the number of handicap patients
df['Diabetes'].value_counts()


# Counting the Hipertension patients

# In[45]:


#Counting the Hipertension patients
df['Hipertension'].value_counts()


# which disease is more dominant among patients

# In[46]:


#which disease is more dominant among patients
x=["Hipertension","Diabetes","Handcap"]
y=[2042+183+13+3,7943,21801]
plt.pie(y,labels=x,autopct='%1.1f%%')
circle = plt.Circle(xy=(0, 0), radius=0.75, facecolor="white")
plt.gca().add_artist(circle)
plt.title("Diseases percetanges among patients")


# Conclusoin:* The number of females generally i  omre than males, female patients are more than male. 
# Also healthy females are more than males. 
# *The most dense neighbourhood is Jardim Camburi
# Limiatations: we can not invesitage for sure about the reasons the patients didnt show up. 
#     we can not investigate if the patients are satisified about the health care service provided.
# 
#     
