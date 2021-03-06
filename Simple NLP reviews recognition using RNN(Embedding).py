# -*- coding: utf-8 -*-
"""Simple NLP reviews recognition using RNN(Embedding).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/126IIZvtNmID7W2NiC48BJxrt4Uk4rHdG
"""

import numpy as np
from tensorflow import keras

reviews = ['nice food',
           'amazing resturant',
           'too good',
           'just loved it!',
           'will go again',
           'horrible food',
           'never go there again',
           'poor service',
           'poor quality',
           'need improvement',
           ]

sentiment = np.array([1,1,1,1,1,0,0,0,0,0])

voc_size = 500
encoded_reviews = [keras.preprocessing.text.one_hot(i, voc_size) for i in reviews]

encoded_reviews

max_length = 4
embedded_reviews = keras.preprocessing.sequence.pad_sequences(encoded_reviews, maxlen = 4, padding = 'post')

embedded_reviews

model = keras.Sequential()
model.add(keras.layers.Embedding(voc_size, voc_size, input_length = max_length, name = 'embedding'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

X = embedded_reviews
y = sentiment

model.fit(X, y, epochs=50)

model.evaluate(X, y)

temp_reviews = [
           'horrible resturant',
           'this is so bad',
           'i will not go there again',
           'very high quality',
           'need some improvement',
           'not a good food at all',
           'amazing resturant',
           'too good',
           'just loved it!',
           'fantastic resturant',
           ]

temp_encoded = [keras.preprocessing.text.one_hot(i, 500)for i in temp_reviews]
temp_embedded = keras.preprocessing.sequence.pad_sequences(temp_encoded,maxlen = 4, padding = 'post' )

model.predict(temp_embedded)

