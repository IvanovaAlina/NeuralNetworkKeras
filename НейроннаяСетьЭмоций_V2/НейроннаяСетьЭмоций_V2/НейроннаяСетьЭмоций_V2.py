#3 эпохи rmsporp 10 000 элементов в массиве
#from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import csv
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

#(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=5000)
#print(X_train)
#print(y_train)
#X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
#X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

path_file = "C:/Users/IvanovaAlina/Desktop/Учеба/Диплом/"
file = open(path_file + "dataset_new.csv",encoding ="utf-8")
file_reader = csv.reader(file, delimiter = ";")
lables = []
texts = []
count = 0
for row in file_reader:
    if count > 0:
        lables.insert(count, int(row[1]))
        texts.insert(count, row[0])
    count+=1
data = {
    'label': lables,
    'text' : texts
    }


tknizer = Tokenizer()
tknizer.fit_on_texts(data['text'])
x1 = tknizer.texts_to_sequences(data['text'])
x1 = sequence.pad_sequences(x1, value=0, padding='post', maxlen=50)



# Get X and y matrices
y = np.array(data['label'])
x = np.array(x1)#data['text']

X_train = x[0:10000]
y_train = y[0:10000]
X_test = x[10001:20000]
y_test = y[10001:20000]

print(len(X_train))
print(len(X_test))

max_review_length = 500
embedding_vecor_length = 32
top_words = 100000
model = Sequential()
model.add(layers.Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
model.add (layers.Dropout (0.2))
model.add(layers.LSTM(100))
model.add (layers.Dropout (0.2))
model.add(layers.Dense(250, activation='relu'))
model.add(layers.Dense(1, activation= 'sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.summary()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=64)
scores = model.evaluate(X_test, y_test, verbose=1)
print("Accuracy: %.2f%%" % (scores[1]*100))

