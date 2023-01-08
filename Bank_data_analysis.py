

Agenda = {
    1:"Importing what I want",
    2:"Loading our data",
    3:"Lets look at age column",
    4:"The main question",
    5:"CONCLUSION OF DATA ANALYSIS",
    6:"Data Preprocessing",
    7:"CONCLUSION OF DATA PREPROCESSING",
    8:"Data Preprocessing for Building Models",
    9:"Saving our data"
}

Agenda


# In[2]:


# importing some lib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ignore error
import warnings 
warnings.filterwarnings("ignore")


# In[3]:


import os
print(os.getcwd())


# In[10]:


trans = pd.read_csv("/Users/reenarani/Downloads/test.csv", sep = ";")
print(train.head(5))


# In[6]:


trans = pd.read_csv("/Users/reenarani/Downloads/test.csv", sep = ";")
trans


# In[11]:


trans.head()


# In[8]:


trans.tail()


# In[12]:


trans.info()


# In[14]:


trans.describe()


# In[15]:


np.random.seed(42)
fig = plt.figure(figsize = (5,5))
ax = fig.add_subplot(111)
bp = ax.boxplot(trans["age"] , patch_artist = True,
               notch = True , vert = 0)
plt.show()


# In[16]:


sns.kdeplot(train.age, cumulative = True)


# In[17]:


string_columns = list(train.dtypes[trans.dtypes == "object"].index)
string_columns


# In[18]:


for i in trans.columns:
    if i in string_columns:
        results = trans[i].value_counts()
        print(results, "\n")
        print("-/"*20, "\n")


# In[19]:


#The main question is what are the most characteristic features of the people who respond to the campaign and register for deposits?
#Now we will try to dig into that data in order to extract accurate answers to this question. 
#The answer may not be complete, but I will try to answer it accurately.

trans["balance"].max(), trans["balance"].min()


# In[20]:


sns.set(rc={"figure.figsize":(8, 8)})
sns.jointplot(x = trans.age, y = trans.balance)


# In[21]:


manage = trans[(trans["job"] == "management")]
print(len(manage))


# In[22]:


sns.set(rc={"figure.figsize":(5, 5)})
sns.histplot(manage["y"])


# In[23]:


manage_yes = manage[manage["y"] == "yes"]


# In[24]:


sns.histplot(manage_yes["marital"])


# In[27]:


sns.histplot(manage["marital"])


# In[28]:


sns.set(rc={"figure.figsize":(8, 8)})
sns.jointplot(x = train.age, y = train.balance)


# In[29]:


trans["education"].value_counts()


# In[30]:


sns.jointplot(x = "balance", y = "age",
             hue = "education",
             data = trans)


# In[35]:


trans.groupby("y").first()


# In[36]:


trans["job"].value_counts()


# In[37]:


trans[trans["job"]=="admin."].groupby("y").first()


# In[40]:


trans[trans["job"]=="services"].groupby("y").first()


# In[41]:


trans[trans["job"]=="student"].groupby("y").first()


# In[42]:


trans[trans["job"]=="retired"].groupby("y").first()


# In[44]:


admin = train[(train["job"] == "technician")]
print(len(manage))

sns.histplot(technician["y"])


# In[45]:


technician_yes = technician[technician["y"] == "yes"]
len(technician_yes)


# In[48]:


admin_yes = admin[admin["y"] == "yes"]
len(admin_yes)


# In[49]:


sns.histplot(admin_yes["education"])


# In[50]:


trans["housing"].value_counts()


# In[51]:


sns.stripplot(trans.housing, # it it x axis
             trans.balance,    # it is y axis
             hue = trans.y)


# In[52]:


sns.jointplot(x = "balance", y = "age",
             hue = "housing",
             data = trans)


# In[57]:


trans["pdays"].value_counts().head(20)


# In[58]:


sns.jointplot(x = "pdays", y = "balance",
             hue = "y",
             data = trans)


# In[59]:


the_most_frec = trans[trans["pdays"] == -1]
the_most_frec.head()


# In[60]:


the_most_frec["y"].value_counts().plot.bar()


# In[61]:


def default_to_num(df):
    if df['default'] == 'no':
        return 0
    elif df['default'] == 'yes':
        return 1
    else:
        return 99


# In[62]:


trans['default'] = trans.apply(default_to_num, axis=1)
trans["default"].value_counts()


# In[63]:


trans["loan"] = trans.apply(loan_to_num, axis = 1)
trans["loan"].value_counts()


# In[64]:


data = trans.drop(['month','day'],axis=1)
data.head()


# In[65]:


bin_values = np.arange(start = 0 , stop = 100 , step = 1)

data["age"].hist(bins=bin_values)


# In[66]:





# In[67]:





# In[73]:


Q1 = trans.age.quantile(0.25)
Q3 = trans.age.quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5*IQR+10
upper_limit = Q3 + 1.5*IQR
lower_limit, upper_limit


# In[75]:


# removing outliers
df_no_outlier = data[(data.age>lower_limit)&(data.age<upper_limit)]
df_no_outlier.head()


# In[74]:


data[(data.age<lower_limit)|(data.age>upper_limit)].head()


# In[72]:


#9. Saving our data
#Saving our data with CSV extension

trans.to_csv("final_version.csv")


# In[ ]:




