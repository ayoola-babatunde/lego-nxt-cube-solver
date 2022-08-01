#%%
import glob
from helpfns import get_dominant_color, show_color, get_cubies,  bgr2lab
import cv2
import pandas as pd
from sklearn.cluster import KMeans
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from takepix import take_pics
from colorsys import rgb_to_hsv
import numpy as np

#%%
def frame_to_bgrhsvlab(frame): 
    bgr = get_dominant_color(frame)
    hsv = rgb_to_hsv(bgr[2]/255, bgr[1]/255, bgr[0]/255)
    lab = np.array(bgr2lab(bgr))/100

    bgr_hsv_lab = [bgr/255, hsv, lab]
    return [x for xs in bgr_hsv_lab for x in xs]



# %%
colors = ['blue2', 'green2', 'orange2', 'red2', 'white2', 'yellow2']

all_dom_cols = []

for col in tqdm(colors): 
    for filename in glob.glob(f"C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/Cubies2/{col}/*.png"): 
        pixels = cv2.imread(filename)
        all_dom_cols.append(frame_to_bgrhsvlab(pixels) + [col])

#%%
#train with non-brightly lit pics
for col in tqdm(colors): 
    for filename in glob.glob(f"C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/Cubies/{col[:-1]}/*.png"): 
        pixels = cv2.imread(filename)
        all_dom_cols.append(frame_to_bgrhsvlab(pixels) + [col])

# %%
df = pd.DataFrame(all_dom_cols, columns=['b', 'g', 'r', 'h', 's', 'v', 'l', 'a', 'b_', 'color'])
df['color'] = df['color'].astype('category')
df['color_cat'] = df['color'].cat.codes

color_dict = dict(enumerate(df['color'].cat.categories))

#%%
#hsv_values = [rgb_to_hsv(x[2], x[1], x[0]) for x in df.values]

#df =  df.join(pd.DataFrame(hsv_values, columns=['h', 's', 'v']))
#%%

X_train, X_test, y_train, y_test = train_test_split(df[['b', 'g', 'r', 'h', 's', 'v', 'l', 'a', 'b_']], df['color_cat'], test_size=0.33)

#%%
log_reg_model = LogisticRegression(class_weight='balanced')
log_reg_model.fit(X_train, y_train)

#%%
predictions = log_reg_model.predict(X_test)
# %%
log_reg_model.score(X_test, y_test)

# %%

faces_path = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/'
test_im = cv2.imread(faces_path + 'o44433.png')
test_cubies = [x for x in get_cubies(test_im, False)]
# %%
test_dom_cols = [np.array(frame_to_bgrhsvlab(x)) for x in test_cubies]
# %%

pred_test_dom_cols = [color_dict[log_reg_model.predict(x.reshape(1, -1))[0]][0] for x in test_dom_cols]

#%%
faces_path = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/'
red_face = cv2.imread(faces_path + 'r4.png')
orange_face = cv2.imread(faces_path + 'o4.png')
green_face = cv2.imread(faces_path + 'g4.png')
blue_face = cv2.imread(faces_path + 'b4.png')
yellow_face = cv2.imread(faces_path + 'y4.png')
white_face = cv2.imread(faces_path + 'w4.png')

all_faces = [yellow_face, blue_face, red_face, green_face, orange_face, white_face]
# %%
all_pred_col = []
for face in tqdm(all_faces): 
    dom_col_cubies = [np.array(frame_to_bgrhsvlab(x)) for x in get_cubies(face, False)]
    pred_cols = [color_dict[log_reg_model.predict(x.reshape(1, -1))[0]][0] for x in dom_col_cubies]
    all_pred_col.append(pred_cols)

# %%
state = "".join([x for xs in all_pred_col for x in xs])
# %%
