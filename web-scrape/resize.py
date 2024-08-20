from PIL import Image
import os.path

for city in ['Paris', 'Toronto', 'LosAngeles']:
    for i in range(300):
        if os.path.isfile(city + '/' + str(i) + '.png'):
            im = Image.open(city + '/' + str(i) + '.png')
            im = im.crop((0, 0, 2500, 950))
            im = im.resize((256, 256))
            im.save(city + 'Resized/' + str(i) + '.png')
