#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
print(os.listdir())


# In[2]:


import pandas as pd

# Load file and skip top 2 rows
df = pd.read_excel("deep learning.xlsx", header=2)

print(df.head())


# In[3]:


import pandas as pd

# Load normally (no header)
df = pd.read_excel("deep learning.xlsx", header=None)

# Use first row as column names
df.columns = df.iloc[0]

# Remove that first row from data
df = df[1:]

# Reset index
df = df.reset_index(drop=True)

print(df.head())


# In[4]:


import pandas as pd

# Skip top 3 rows completely
df = pd.read_excel("deep learning.xlsx", skiprows=3)

print(df.head())


# In[5]:


# Rename column
df.rename(columns={"Student Name": "Name"}, inplace=True)

# Drop unnecessary columns
df = df.drop(columns=["Sr.", "Reg. Number", "Total P"])

print(df.head())


# In[6]:


df.replace({'P': 1, 'A': 0}, inplace=True)

print(df.head())


# In[7]:


df.replace({'P': 1, 'A': 0}, inplace=True)

print(df.head())


# In[8]:


df.rename(columns={"Student Name": "Name"}, inplace=True)


# In[9]:


df = df.drop(columns=["Sr.", "Reg. Number", "Total P"], errors='ignore')


# In[10]:


print(df.columns)


# In[11]:


print(df.head())
print(df.dtypes)


# In[12]:


import numpy as np

names = df['Name']
attendance = df.drop('Name', axis=1)

X = []
y = []

for row in attendance.values:
    X.append(row[:-1])   # input sequence
    y.append(row[-1])    # target

X = np.array(X)
y = np.array(y)


# In[13]:


X = X.astype('float32')
y = y.astype('float32')


# In[14]:


X = X.reshape((X.shape[0], X.shape[1], 1))

print("X shape:", X.shape)
print("y shape:", y.shape)


# In[15]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

model = Sequential()

model.add(SimpleRNN(16, input_shape=(X.shape[1], 1)))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()


# In[16]:


model.fit(X, y, epochs=50, batch_size=2)


# In[17]:


def predict_attendance(student_name):
    if student_name not in list(names):
        print("❌ Student not found")
        return

    idx = names[names == student_name].index[0]
    student_data = attendance.iloc[idx].values

    print("📊 Past Attendance:", student_data)

    # reshape
    input_data = np.array(student_data[:-1]).reshape(1, -1, 1)

    prediction = model.predict(input_data)

    prob = prediction[0][0]

    print("📊 Probability:", prob)

    if prob > 0.5:
        print("✅ Next Day Prediction: Present")
    else:
        print("❌ Next Day Prediction: Absent")


# In[19]:


predict_attendance("RAFIA REHMAN")


# In[ ]:




