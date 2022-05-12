# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:28:23 2022

@author: oby_pc
"""

import tensorflow as tf
from tensorflow.keras import models, layers
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pathlib
import os

# to disable all debugging logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#importing data set
dir =os.listdir('D:\\belgelerim\\programing\\4_Data_Projects\\ML_Patato_early_blight')
for filenames in dir:
    print(filenames)

Current_Dir = os.getcwd()
dataset_dir = pathlib.Path(Current_Dir)
print(dataset_dir)

Image_Size = 256
Batch_Size = 32
Channels = 3
Epochs = 50

dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_dir, batch_size = Batch_Size, image_size = (Image_Size, Image_Size), shuffle = True) 



class_name = dataset.class_names
class_name

len(dataset)


#prints Elements in dataset: here 1st element is image and 2nd index of that image.

print(dataset)

# Plotting the image
plt.figure(figsize = (15,15))
# dataset.take(count) : Creates a Dataset with at most 'count' elements(batch) from the dataset
for image, label in dataset.take(1): 
    for i in range(12):
        plt.subplot(3, 4, i+1) # many plots at a time =>subpots
        plt.imshow(image[i].numpy().astype('uint8')) #converting all data of image into numpy and than to intiger type as they were in float.
        plt.title(class_name[label[i]])  # title of the class_name of image
        plt.axis("off") # Hide the values of graph
     




# PLotting Image
plt.figure(figsize = (20,20))

#dataset.take(Count): Creates a dataset with at most 'count' elements(batch) from dataset

for image, label in dataset.take(1):
    for i in range (12):
        plt.subplot(3, 4, i+1) # many plot at a time  ==> subplot
        #converting all data of image into numpy and than to intiger type as they were in float.
        plt.imshow(image[i].numpy().astype('uint8'))
  
        # title of the class_name of image
        plt.title(class_name[label[i]])
        
        # Hide the values of graph
        plt.axis('off')


# Function for Splitting the data

def split_dataset(ds, train_split=0.8, val_split=0.1, test_split=0.1, shuffle=True, shuffle_size=1000):
    if shuffle:
        ds = ds.shuffle(shuffle_size, seed = 10)
        
    ds_size = len(ds)
    train_size =int(train_split * ds_size)
    val_size = int(val_split * ds_size)
    
    train_ds = ds.take(train_size)
    val_ds = ds.skip(train_size).take(val_size)
    test_ds = ds.skip(train_size).take(val_size)
    
    return train_ds, val_ds, test_ds


train_data, val_data, test_data = split_dataset(dataset)


print("Size of Data is: {0} \nBatch size of Training Data is:{1}\nBatch size of Val data is:{2}\nBatch size of Test Dast Is:{3} " .format(len(dataset), len(train_data), len(val_data), len(test_data)))



# caching,shuffle and prefetching the data

train_ds = train_data.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)
val_da = val_data.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)
test_ds = test_data.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)



# Image Preprocessing : Rescaling and Resizing

resize_and_rescale = tf.keras.Sequential([
    layers.experimental.preprocessing.Resizing(Image_Size, Image_Size),
    layers.experimental.preprocessing.Rescaling(1.0/255)
])



# Data augmentation by flipping and rotating existing images

data_augmentation = tf.keras.Sequential([
    layers.experimental.preprocessing.RandomFlip(mode = "horizontal_and_vertical"),
    layers.experimental.preprocessing.RandomRotation(factor = 0.2)
])




# Creating Convolution Layers

input_shape = (Batch_Size, Image_Size, Image_Size, Channels)
model = models.Sequential([
    resize_and_rescale,
    data_augmentation,
    layers.Conv2D(filters = 32, kernel_size = (3,3), activation = 'relu', input_shape = input_shape),
    layers.MaxPool2D((2,2)),
    layers.Conv2D(64, (3,3), activation = 'relu'),
    layers.MaxPool2D((2,2)),
    layers.Conv2D(64, (3,3), activation = 'relu'),
    layers.MaxPool2D((2,2)),
    layers.Conv2D(64, (3,3), activation = 'relu'),
    layers.MaxPool2D((2,2)),
    layers.Conv2D(64, (3,3), activation = 'relu'),
    layers.MaxPool2D((2,2)),
    layers.Conv2D(64, (3,3), activation = 'relu'),
    layers.MaxPool2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation = 'relu'),
    layers.Dense(64, activation = 'softmax'),

])


model.build(input_shape = input_shape)































