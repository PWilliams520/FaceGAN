import urllib.request
import tarfile
import os
from keras.datasets import cifar10
from keras.utils import np_utils

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# convert class vectors to binary vectors
Y_train = np_utils.to_categorical(y_train)
Y_test = np_utils.to_categorical(y_test)

print('X_train shape:', X_train.shape)
print('Y_train shape:', Y_train.shape)
print('X_test shape:', X_test.shape)
print('Y_test shape:', Y_test.shape)

# dataset path
home = os.path.expanduser('~')
data_path = os.path.join(home, "data/CIFAR-10/")
data_url = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"

# CIFAR-10 constants
img_size = 32
img_channels = 3
nb_classes = 10
# length of the image after we flatten the image into a 1-D array
img_size_flat = img_size * img_size * img_channels
nb_files_train = 5
images_per_file = 10000
# number of all the images in the training dataset
nb_images_train = nb_files_train * images_per_file


def download_and_extract_cifar():
    if not os.path.exists(data_path):
        os.makedirs(data_path)

        file_path, _ = urllib.request.urlretrieve(url=data_url,
                                                  filename=os.path.join(data_path, 'cifar-10-python.tar.gz'),
                                                  reporthook=None)
        print('\nExtracting... ', end='')
        tarfile.open(name=file_path, mode="r:gz").extractall(data_path)
        print('done')
    else:
        print("Data has already been downloaded and unpacked.")


download_and_extract_cifar()