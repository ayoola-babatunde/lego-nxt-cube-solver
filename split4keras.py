#%%
import glob
import cv2
from matplotlib.pyplot import get
from helpfns import get_cubies
import random
import os
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout
import pandas as pd
from tqdm import tqdm
# %%
save_in = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/Cubies2'

image_list = []
for filename in glob.glob("C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/*.png"): 
    image_list.append(filename)

# %%
for image in tqdm(image_list): 
    #print(image)
    cubies = get_cubies(cv2.imread(image), False)
    for cubie in cubies: 
        cv2.imwrite(f'{save_in}/{random.randint(1,100000)}.png', cubie)
    #get_cubies(frame)

    
# %%
all_cubies = []
for cubie in glob.glob("C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/Cubies2/*.png"): 
    all_cubies.append(cubie)
# %%

for cubie in tqdm(all_cubies): 
    image = cv2.imread(cubie)
    cv2.imshow('', image)
    k = cv2.waitKey()

    if k == ord('g'): 
        cv2.imwrite(f'{save_in}/green2/{random.randint(1,100000)}.png', image)
    if k == ord('b'): 
        cv2.imwrite(f'{save_in}/blue2/{random.randint(1,100000)}.png', image)
    if k == ord('o'): 
        cv2.imwrite(f'{save_in}/orange2/{random.randint(1,100000)}.png', image)
    if k == ord('r'): 
        cv2.imwrite(f'{save_in}/red2/{random.randint(1,100000)}.png', image)
    if k == ord('w'): 
        cv2.imwrite(f'{save_in}/white2/{random.randint(1,100000)}.png', image)
    if k == ord('y'): 
        cv2.imwrite(f'{save_in}/yellow2/{random.randint(1,100000)}.png', image)
    if k == 27: 
        cv2.destroyAllWindows()

# %%
#training a keras model

data_dir = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/Cubies2/'
labels = ['green2', 'blue2', 'orange2', 'red2', 'white2', 'yellow2']

data = []
labels_int = []
for label in tqdm(labels): 
    path = os.path.join(data_dir, label)
    class_num = labels.index(label)
    for img in os.listdir(path): 
        try: 
            img_arr = cv2.imread(os.path.join(path, img))[...,::-1]
            data.append(img_arr)
            labels_int.append(class_num)
        except Exception as e: 
            print(e)
# %%
X_train, X_test, y_train, y_test = train_test_split(data, labels_int, test_size=0.33, random_state=42)

# %%
# Normalize the data
img_size = 100
X_train = np.array(X_train)/255
X_test = np.array(X_test)/255

X_train.reshape(-1, img_size, img_size, 1)
y_train = np.array(y_train)

X_test.reshape(-1, img_size, img_size, 1)
y_test = np.array(y_test)

# %%
model = Sequential()
model.add(Conv2D(25, (3,3), input_shape = (100,100,3)))
model.add(MaxPool2D(pool_size=(1,1)))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.4))
# output layer
model.add(Dense(6, activation='softmax'))


model.summary()
# %%
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# %%
history = model.fit(X_train,y_train,epochs = 20 , validation_data = (X_test, y_test))
#%%
#more testing with live data
faces_path = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/'
test_im = cv2.imread(faces_path + 'o44433.png')
test_cubies = [x for x in get_cubies(test_im, False)]
# %%

cols = {0:'g', 1:'b', 2:'o', 3:'r', 4:'w', 5:'y'}
pd.Series([np.argmax(model.predict(x)) for x in test_cubies]).map(cols)
# %%
#more tests
test_single_cubie = cv2.imread(faces_path + 'Cubies2/37058.png')
tss = test_single_cubie.reshape(-1, img_size, img_size, 3)/255
np.argmax(model.predict(tss))
# %%


#%%
#k means clustering
X_train = (np.array(X_train)).reshape(len(X_train), -1)
X_test = (np.array(X_test)).reshape(len(X_test), -1)

# %%
