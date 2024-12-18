# Loading the data set file
import pandas as pd
df=pd.read_csv("/content/Data required for the assignmnet.csv")
df.head()

# Fill all the missing values from features
import numpy as np
df=df.fillna(0)
print(df.isnull().sum().sum())

# Taking input to the user about starting and ending time
start_time=int(input("Enter the starting time: "))
end_time=int(input("Enter the ending time: "))

from datetime import time,datetime
import time
df=pd.DataFrame(df)
data={}

# creating a function for insert the dataframe into dictnory
def insert(timestp,city,value):
  if city not in data:
    data[city]={}
  if timestp in data:
    data[city][timestp].append(value)
  else:
    data[city][timestp]=[value]

# here i am using linersearch and its time complexity is O(n)
def linersearch(arr,x):
  for i in range(len(arr)):
    if arr[i]==x:
      return i
  return -1


def get_stats(city,start_time,end_time):
  timestp=sorted(data[city].keys())
  start_index=interpolation_search(timestp,0,len(timestp)-1,start_time)
  end_index=interpolation_search(timestp,0,len(timestp)-1,end_time)
  if start_index==-1 or end_index==-1:
    return 0,0,0,0

  sumval=0
  minval=float('inf')
  maxval=float('-inf')
  count=0
  for i in range(start_index,end_index+1):
      sumval+=sum(data[city][timestp[i]])
      count+=len(data[city][timestp[i]])
      minval=min(minval,min(data[city][timestp[i]]))
      maxval=max(maxval,max(data[city][timestp[i]]))

  if count>0:
     meanval=sumval/count
  else:
    meanval=0
  return sumval,meanval,minval,maxval

for index,row in df.iterrows():
  for city in ['Mumb','Chennai','Khar','Delh']:
      insert(row['timestamp'],city,row[city])

# timer is use for showimg the complexity or we can say time exicution for this searching
startingtime=time.time()
for city in ['Mumb','Chennai','Khar','Delh']:
  sumval,meanval,minval,maxval=get_stats(city,start_time,end_time)
  print(f"City: {city}")
  print(f"Sum: {sumval}")
  print(f"Mean: {meanval}")
  print(f"Min: {minval}")
  print(f"Max: {maxval}")
  print()
endingtime=time.time()
print(f"Time taken: {endingtime-startingtime}")

from datetime import time,datetime
import time
df=pd.DataFrame(df)
data={}
def insert(timestp,city,value):
  if city not in data:
    data[city]={}
  if timestp in data:
    data[city][timestp].append(value)
  else:
    data[city][timestp]=[value]

''' here i am using interpolation search because
Complexity: Runtime: The average runtime complexity of interpolation search is
 O(log log N) and has a worst case of O(N),
 which happens when the keys increase exponentially.
 Space: O(1) for initializing variables high, low, mid.'''

def interpolation_search(arr, low, high, x):
   if high >= low:
    # Ensure index is an integer
    index = int(low + ((high - low) // (arr[high] - arr[low])) * (x - arr[low]))
    if index < len(arr) and arr[index] == x: # Check if index is within bounds
      return index
    if index < len(arr) and arr[index] < x: # Check if index is within bounds
      return interpolation_search(arr, index + 1, high, x)
    if index < len(arr) and arr[index] > x: # Check if index is within bounds
      return interpolation_search(arr, low, index - 1, x)
   return -1

def get_stats(city,start_time,end_time):
  timestp=sorted(data[city].keys())
  start_index=interpolation_search(timestp,0,len(timestp)-1,start_time)
  end_index=interpolation_search(timestp,0,len(timestp)-1,end_time)
  if start_index==-1 or end_index==-1:
    return 0,0,0,0

  sumval=0
  minval=float('inf')
  maxval=float('-inf')
  count=0
  for i in range(start_index,end_index+1):
      sumval+=sum(data[city][timestp[i]])
      count+=len(data[city][timestp[i]])
      minval=min(minval,min(data[city][timestp[i]]))
      maxval=max(maxval,max(data[city][timestp[i]]))

  if count>0:
     meanval=sumval/count
  else:
    meanval=0
  return sumval,meanval,minval,maxval

for index,row in df.iterrows():
  for city in ['Mumb','Chennai','Khar','Delh']:
      insert(row['timestamp'],city,row[city])

# timer is use for showimg the complexity or we can say time exicution for this searching
startingtime=time.time()
for city in ['Mumb','Chennai','Khar','Delh']:
  sumval,meanval,minval,maxval=get_stats(city,start_time,end_time)
  print(f"City: {city}")
  print(f"Sum: {sumval}")
  print(f"Mean: {meanval}")
  print(f"Min: {minval}")
  print(f"Max: {maxval}")
  print()
endingtime=time.time()
print(f"Time taken: {endingtime-startingtime}")

"""Hence we can see that the exicution time in interpolation search get reduced if we using linear search instead of interpolation its taken more time"""
