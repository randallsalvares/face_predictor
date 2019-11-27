#!/usr/bin/env python
# coding: utf-8

# In[19]:


# import the necessary packages
import numpy as np
import urllib
import cv2

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image


# In[22]:


image=url_to_image("https://hackattic.com/_/faces/71041770.0256.4a41.ac56.fe710cef4030") #here enter the image url


# In[24]:


plt.figure(figsize = (15,15))
plt.imshow(image) #view the image, since matplotlib has imageBGR we have a bluish tint to it.


# In[25]:


image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #change the bluish BGR to RGB
plt.figure(figsize = (15,15))
plt.imshow(image)#see the original image


# In[26]:


#Converting to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to black and white for faster computation and processing

# Displaying the grayscale image
plt.figure(figsize = (15,15))
plt.imshow(image_gray, cmap='gray')


# In[28]:


haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #import and load the haar face cascade from online


# In[30]:


faces_rec= haar_cascade_face.detectMultiScale(image_gray, scaleFactor = 1.2, minNeighbors = 5);#we use detectMultiScale funtion to detect faces

# Let us print the no. of faces found
print('Faces found: ', len(faces_rec))#it returns a x,y,w,h coordinates of the rectangles in the image


# In[31]:


faces_rec #we will use the first 2 columns to identify the location of rectangles in the image tiles later


# In[32]:


for (x,y,w,h) in faces_rec:
     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 255), 2) #draw rectangles on the faces as per the x,y,w,h coordinates


# In[33]:


plt.figure(figsize = (15,15))
plt.imshow(image)


# In[38]:


#make 2 lists of X and y coordinates
x_values = faces_rec[:,0] 
y_values = faces_rec[:,1]


# In[39]:


x_values


# In[40]:


y_values


# In[41]:


import math #import math for making the round up function for the X and Y coordinates shown below
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


# In[42]:


#here all the X values are divided by 100 then deducted by 1 and rounded up, if the values are less than 100 they are
#taken as 0
for x in range(len(faces_rec)):
    if x_values[x]<100:
        x_values[x]=x_values[x]-x_values[x]
    else:
        x_values[x]=round_up((x_values[x]/100)-1)
        
x_values


# In[43]:


#here all the Y values are divided by 100 then deducted by 1 and rounded up, if the values are less than 100 they are
#taken as 0
for y in range(len(faces_rec)):
    if y_values[y]<100:
        y_values[y]=y_values[x]-y_values[x]
    else:
        y_values[y]=round_up((y_values[y]/100)-1)
        
y_values


# In[46]:


#now we have the values for the coordinates pointing to the tiles that have a face in them as shown below
face_tiles = []
for i in range(len(faces_rec)):
    face_tiles.append([x_values[i], y_values[i]])
face_tiles


# In[ ]:




