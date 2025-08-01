import os
import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
# Model has been made with following commented script
# print(tf.__version__)
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis= 1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
# model.add(tf.keras.layers.Dense(128, activation= "relu"))

# model.add(tf.keras.layers.Dense(128, activation= "relu"))
# model.add(tf.keras.layers.Dense(10, activation= "softmax"))

# model.compile(optimizer= "adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# model.fit(x_train, y_train, epochs=3)
# model.save("Handwritten_Model")

model = tf.keras.models.load_model("Handwritten_Model")

image_num = 1
while os.path.isfile(f"Numbers/{image_num}.png"):
    try:
        img = cv2.imread(f"Numbers/{image_num}.png")[:,:,0]
        img = np.invert(np.array([img]))
        pred = model.predict(img)
        print(f"The number is {np.argmax(pred)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()

    finally:

        image_num +=1
