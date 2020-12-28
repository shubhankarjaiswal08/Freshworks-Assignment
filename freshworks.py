#!/usr/bin/env python
# coding: utf-8

# In[29]:


import threading 
from threading import*
import time

jsonobject={} #'json object' is just like dictionary in which we store data


def create(key,value,timeout=0):
    if key in jsonobject:
        print("error: this key already exists")
    else:
        if(key.isalpha()):
            if len(jsonobject)<(1024*1020*1024) and value<=(16*1024*1024): #file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    jsonobject[key]=l
            else:
                print("error: exceeded memory encountered! ")
        else:
            print("error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers")


            
def read(key):
    if key not in jsonobject:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        newb=jsonobject[key]
        if newb[1]!=0:
            if time.time()<newb[1]: 
                strinng=str(key)+":"+str(newb[0]) 
                return strinng
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            strinng=str(key)+":"+str(newb[0])
            return strinng


def delete(key):
    if key not in jsonobject:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        abc=jsonobject[key]
        if abc[1]!=0:
            if time.time()<abc[1]: 
                del jsonobject[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del jsonobject[key]
            print("key is successfully deleted")


def changeto(key,value):
    a=jsonobject[key]
    if a[1]!=0:
        if time.time()<a[1]:
            if key not in jsonobject:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(a[1])
                jsonobject[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in jsonobject:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            l=[]
            l.append(value)
            l.append(a[1])
            jsonobject[key]=l


# In[32]:


create("shubhankar",25,3600)


create("freshworks",70,3600) 



read("shubhankar")


read("freshworks")

read("taj mahal")

create("shubhankar",50,3600)

create("jaiswal",69,3600)

changeto("shubhankar",55)

changeto("freshworks",79)

delete("shubhankar")



t1=threading.Thread(target=(create or read or delete),args=("shubhankar",50)) 

t2=threading.Thread(target=(create or read or delete),args=("shubhankar",60))

t3=threading.Thread(target=(create or read or delete), args =("jaiswal",55))

t4=threading.Thread(target=(create or read or delete), args =("jaiswal",69))


t1.start()

 
t2.start()

t3.start()


t1.join()

t2.join()

t3.join()


# In[ ]:




