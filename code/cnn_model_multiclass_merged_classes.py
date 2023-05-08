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

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(256, 256, 3)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense((33)))
model.add(Softmax())

model.compile(loss = keras.losses.categorical_crossentropy, optimizer='adam', metrics=['categorical_accuracy'])

model.summary()

# TO GRAYSCALE IMAGES

def to_grayscale(image):
    image = tensorflow.image.rgb_to_grayscale(image)
    return image

# TRAIN GENERATORS

print("Retrieving data and generating trainers ...")

data_generator = image.ImageDataGenerator(rescale=1./255, preprocessing_function=to_grayscale)

# RETRIEVING IMAGE NAMES AND ASSOCIATED LABELS
train_df = pd.read_csv("/path_to_your_df/final_training_dataset_oversampled.csv")
test_df = pd.read_csv("/path_to_your_df/final_test_dataset_oversampled.csv")

train_generator = data_generator.flow_from_dataframe(directory='/path_to_your_images', target_size=(256, 256), shuffle=False, batch_size = 32, class_mode = 'categorical', dataframe = train_df, x_col = 'Filenames', y_col = 'labels', validate_filenames=False)

test_generator = data_generator.flow_from_dataframe(directory='/path_to_your_images', target_size=(256, 256), shuffle=False, batch_size = 32, class_mode = 'categorical', dataframe = test_df, x_col = 'Filenames', y_col = 'labels', validate_filenames=False)

# FITTING MODEL

print("Fitting model ...")

e_s = EarlyStopping(monitor='val_loss', patience = 1)
history = model.fit(train_generator, steps_per_epoch=len(train_generator), epochs=15, callbacks=[e_s], validation_data=test_generator)

model.save('/path_to_your_models_directory/model_multiclass_33classes_256_256.h5')

print("Training finished, model saved.")
