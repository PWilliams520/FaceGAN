import os
import tensorflow as tf

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name.endswith("pgm"):
                r.append(os.path.join(root, name))
    return r

def parse(filename, label):
  image_string = tf.read_file(filename)
  image_decoded = tf.image.decode_jpeg(image_string)
  return image_decoded, label

path = "CroppedYale/"

r = []
i = 0
for item in (os.walk(path)):
    i+=1
    s = []
    if len(item[2]) > 1:
        for file in item[2]:
            if file.endswith("pgm"):
                s.append(file)
    if len(s) > 1:
        r.append(s)

# print([x for x in r])

labels = tf.constant([1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39])
labels2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]

filenames = []
labels3 = []
for i in range(len(r)):
    for file in r[i]:
        # print(parse(file, labels[i]))
        filenames.append(file)
        labels3.append(labels2[i])

print(filenames)
print(labels3)
