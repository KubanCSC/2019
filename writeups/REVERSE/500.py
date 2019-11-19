import json

import numpy as np
import tensorflow as tf
from PIL import Image
from matplotlib import pyplot as plt

image = Image.open('flag.png')
with open('flag.json', 'r') as fp:
    flag_array = np.array(json.load(fp))
assert (image.height, image.width) == (75, 1010), 'flag.png should be 1004*73 pixels'
vgg = tf.keras.applications.VGG19(input_shape=(75, 1010, 3),
                                  include_top=False,
                                  weights='imagenet',
                                  pooling=None)
vgg.trainable = False
model = tf.keras.models.Model(vgg.input, vgg.get_layer('block5_conv1').output)
image = np.array(image)[np.newaxis, :, :, :3] / 255
image_array = model(image)
l1_error = tf.reduce_sum(tf.square(image_array - flag_array))
print(f'L1 error between images: {l1_error}\nMinimize it to get the original image!')
# https://medium.com/tensorflow/neural-style-transfer-creating-art-with-deep-learning-using-tf-keras-and-eager-execution-7d541ac31398
##################################################################

init_image = tf.Variable(image, dtype=tf.float32)
opt = tf.keras.optimizers.Adam(learning_rate=0.05)
for i in range(200):
    with tf.GradientTape() as tape:
        style_output_features = model(init_image)
        loss = tf.reduce_sum(tf.abs(style_output_features - flag_array))
    grads = tape.gradient(loss, init_image)
    opt.apply_gradients([(grads, init_image)])
    init_image.assign(tf.clip_by_value(init_image, 0, 1))
    if i % 20 == 0:
        print(f'Iteration: {i}, loss: {loss}')
        plt.figure(figsize=(15, 5))
        plot_img = init_image[0].numpy()
        plt.imshow(plot_img)
        plt.show()
