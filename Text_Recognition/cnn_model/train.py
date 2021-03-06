import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPool2D
from tensorflow.keras import optimizers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import keras

# MNIST Dataset

(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# Removing Noise

_, X_train_th = cv2.threshold(X_train, 127, 255, cv2.THRESH_BINARY)
_, X_test_th = cv2.threshold(X_test, 127, 255, cv2.THRESH_BINARY)

# Reshape

X_train = X_train_th.reshape(-1, 28, 28, 1)
X_test = X_test_th.reshape(-1, 28, 28, 1)

# Categorical output from 0 to 9

y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# print(X_train.shape, y_train.shape)
# print(X_test.shape, y_test.shape)

# Creating CNN model

input_shape = (28, 28, 1)
number_of_classes = 10

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))

model.add(Dropout(0.5))
model.add(Dense(number_of_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=optimizers.Adadelta(), metrics=['accuracy'])

#model.summary()

history = model.fit(X_train, y_train, epochs=5, shuffle=True, batch_size=200, validation_data=(X_test, y_test))

model.save("digit_classifier.h5")
