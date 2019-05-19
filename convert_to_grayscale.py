from PIL import Image
img = Image.open('test-images/test/MVI_05320004.JPG').convert('L')
img.save('greyscale.png')