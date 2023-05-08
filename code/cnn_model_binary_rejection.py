# IMPORTATIONS

print("Importing librairies ...")

import tensorflow 
import os
import numpy as np
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image
import pandas as pd
from keras.callbacks import EarlyStopping


# MODEL INITIALIZATION

print("Initializing model ...")

model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(256, 256, 3)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4,4)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4,4)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4,4)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(loss = keras.losses.binary_crossentropy, optimizer='adam', metrics=['accuracy'])

model.summary()

# TO GRAYSCALE IMAGES

def to_grayscale(image):
    image = tensorflow.image.rgb_to_grayscale(image)
    return image

# TRAIN GENERATORS

print("Retrieving data and generating trainers ...")

data_generator = image.ImageDataGenerator(rescale=1./255, preprocessing_function=to_grayscale)


train_df = pd.read_csv("/path_to_your_df/training_df_for_binary_rejection_balanced.csv")
test_df = pd.read_csv("/path_to_your_df/test_df_for_binary_rejection_balanced.csv")

print(train_df)
print(test_df)

train_generator = data_generator.flow_from_dataframe(directory='/path_to_your_images', target_size=(256, 256), shuffle=False, batch_size = 48, class_mode = 'raw', dataframe = train_df, x_col = 'Filenames', y_col = 'labels', validate_filenames=False)

test_generator = data_generator.flow_from_dataframe(directory='/path_to_your_images', target_size=(256, 256), shuffle=False, batch_size = 48, class_mode = 'raw', dataframe = test_df, x_col = 'Filenames', y_col = 'labels', validate_filenames=False)

# FITTING MODEL

print("Fitting model ...")

early_stopping = EarlyStopping(patience = 1, monitor = 'val_loss')
history = model.fit(train_generator, steps_per_epoch=len(train_generator), epochs=15, validation_data=test_generator, callbacks = [early_stopping])

model.save('/path_to_your_models/model_binary_rejector_256_256.h5')

print("Model trained succesfully and saved.")
