import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import RMSprop
from keras.utils import to_categorical

from PIL import Image
import numpy as np

batch_size = 128
num_classes = 2
epochs = 15

MAGIC_CONSTANT = 1000
# 50x11 image
i = Image.open("flag2.bmp")
WIDTH = i.width
HEIGHT = i.height

flag = []

for h in range(i.height):
    tmp = []
    for w in range(i.width):
        px = i.getpixel((w,h))
        if px[0] == 255:
            tmp.append(0)
        else:
            tmp.append(1)
    flag.append(tmp)

flag = np.array(flag)

x_train = [flag]*MAGIC_CONSTANT*10
y_train = [1]*MAGIC_CONSTANT*10

x_test = []
y_test = []

# Generate a lot of nonflags
# Random images
for i in range(MAGIC_CONSTANT*10):
    tmp = np.random.rand(HEIGHT, WIDTH)
    r = (tmp > 0.6) * 1
    x_train.append(r)
    y_train.append(0)

# zeros
for i in range(MAGIC_CONSTANT//10):
    tmp = np.random.rand(HEIGHT, WIDTH)
    r = (tmp * 0)
    x_train.append(r)
    y_train.append(0)

# Mashed up flag
for i in range(MAGIC_CONSTANT*10):
    tmp = np.random.rand(HEIGHT, WIDTH)
    r = (tmp > 0.95) * 1
    r = ((r + flag) > 0) * 1
    if (r == flag).all():
        continue
    x_train.append(r)
    y_train.append(0)

# Mashed up flag
for i in range(MAGIC_CONSTANT*10):
    tmp = np.random.rand(HEIGHT, WIDTH)
    r = (tmp > 0.95) * 1
    r = ((flag - r) > 0) * 1
    if (r == flag).all():
        continue
    x_train.append(r)
    y_train.append(0)

# Random test
for i in range(MAGIC_CONSTANT):
    tmp = np.random.rand(HEIGHT, WIDTH)
    r = (tmp > 0.9) * 1
    x_test.append(r)
    y_test.append(0)

# zeros test
for i in range(MAGIC_CONSTANT//100):
    tmp = np.random.rand(HEIGHT, WIDTH)
    r = (tmp * 0)
    x_train.append(r)
    y_train.append(0)

x_test = np.array([flag]*(MAGIC_CONSTANT) + x_train[-MAGIC_CONSTANT:] + x_test)
y_test = np.array([1]*(MAGIC_CONSTANT) + y_train[-MAGIC_CONSTANT:] + y_test)

x_train = np.array(x_train[:-MAGIC_CONSTANT])
y_train = np.array(y_train[:-MAGIC_CONSTANT])

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(Flatten(input_shape=(HEIGHT, WIDTH)))
model.add(Dense(HEIGHT*WIDTH, activation='relu'))
model.add(Dense(HEIGHT*WIDTH, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test), shuffle=True)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save("model2.h5")
