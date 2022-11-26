from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

model= Sequential()
model.add(Dense(64, activation='relu',input_dim=50))
model.add(Dense(28, activation='relu'))
model.add(Dense(10,activation='softmax'))

