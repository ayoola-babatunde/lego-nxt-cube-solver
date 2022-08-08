#%%
import glob
from helpfns import show_color, get_cubies, frame_to_bgrhsvlab
import cv2
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np


# %%
def log_model(train_photos = [1,2,3]):

    #1, 2, 3 are dark, medium, and bright environments respectively
    to_train_with = train_photos

    colors = ['blue', 'green', 'orange', 'red', 'white', 'yellow']
    all_dom_cols = []
    path = "C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Gitfolder/lego-nxt-cube-solver/Faces/Test"

    if 1 in to_train_with: 
        #train with non-brightly lit pics
        for col in tqdm(colors): 
            for filename in glob.glob(f"{path}/Cubies/{col}/*.png"): 
                pixels = cv2.imread(filename)
                all_dom_cols.append(frame_to_bgrhsvlab(pixels) + [col])

    if 2 in to_train_with: 
        #train with medium-lit pics
        for col in tqdm(colors): 
            for filename in glob.glob(f"{path}/Cubies2/{col}2/*.png"): 
                pixels = cv2.imread(filename)
                all_dom_cols.append(frame_to_bgrhsvlab(pixels) + [col])

    if 3 in to_train_with: 
        #train with medium-lit pics
        for col in tqdm(colors): 
            for filename in glob.glob(f"{path}/Cubies3/{col}3/*.png"): 
                pixels = cv2.imread(filename)
                all_dom_cols.append(frame_to_bgrhsvlab(pixels) + [col])


    # %%
    df = pd.DataFrame(all_dom_cols, columns=['b', 'g', 'r', 'h', 's', 'v', 'l', 'a', 'b_', 'color'])
    df['color'] = df['color'].astype('category')
    df['color_cat'] = df['color'].cat.codes

    color_dict = dict(enumerate(df['color'].cat.categories))

    #%%

    X_train, X_test, y_train, y_test = train_test_split(df[['b', 'g', 'r', 'h', 's', 'v', 'l', 'a', 'b_']], df['color_cat'], test_size=0.33)

    #%%
    log_reg_model = LogisticRegression(class_weight='balanced')
    log_reg_model.fit(X_train.values, y_train.values)

    # %%
    log_reg_model.score(X_test.values, y_test.values)

    #%%
    predictions = log_reg_model.predict(X_test.values)
    print(metrics.confusion_matrix(y_test.values, predictions))

    return log_reg_model
