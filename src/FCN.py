from tqdm import tqdm  # Questo importa la barra di avanzamento per monitorare la progressione del ciclo
from skimage.io import imread  # Per leggere le immagini
from skimage.transform import resize  # Per ridimensionare le immagini
import numpy as np  # Per manipolare gli array NumPy
import os  # Per operazioni di sistema, come esplorare le directory


seed = 42
np.random.seed(seed)

IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNELS = 3

TRAIN_PATH = '../training_data/'
TEST_PATH = '../test_data/'

train_ids = next(os.walk(TRAIN_PATH))[1] # = ['horses', 'masks']
test_ids = next(os.walk(TEST_PATH))[1] # = ['horses', 'masks']

x = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
y = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, 1), dtype=bool)


print(tqdm(enumerate(train_ids), total=len(train_ids)))

print('Resizing training images and masks')

for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)):   
    print(n)
    print(id_)
