import skimage
import tensorflow as tf
import os
import numpy as np
import scipy
import cv2


def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, d))]

    print(directories)
    labels = []
    images = []

    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".PNG") or f.endswith(".jpg")]
        for f in file_names:
            images.append(skimage.data.image_fetcher)
            labels.append(int(d))
    return images, labels



ROOT_PATH = "/Users/adria/Sybbure SU20/iPillbox_Pill_Analysis/"
train_data_directory = os.path.join(ROOT_PATH,"src/sampleData/train/")
test_data_directory = os.path.join(ROOT_PATH, "src/sampleData/test/")

images, labels = load_data(test_data_directory)




images = np.array(images)
labels = np.array(labels)



# Print the number of `images`'s elements
print(images.size)



# Print the number of `labels`'s elements
print(labels.size)

# Count the number of labels
print(len(set(labels)))
