#!/usr/bin/env python3.7
##
#Import section
import random
import json
import pickle
import numpy as np 
import nltk 
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
##

##
#Initialising objects needed and variables
lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?','!',',','}','{',']','[']
##

##
#Read intents and tokenise
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list , intent['tag']))
        if intent['tag'] not in classes: 
            classes.append(intent['tag'])
##

#lemmatises words ( shortens to the base word) 
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
#sorts any duplicates out
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words,open('words.pk1','wb'))
pickle.dump(classes,open('classes.pk1','wb'))

#Neural Network pre-processing of data
training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1 
    training.append([bag, output_row])

#shuffling the training data
random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

#neural network model 
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
#softmax gets percentages of how likely is for the name to be what we are lookin for
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5 ,verbose=1)
#save model locally 
model.save('cyberbotmodel.h5', hist)
print("Done")
