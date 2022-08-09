#%%
from rubik_solver import utils
import pandas as pd
import takepix
import cv2
from tqdm import tqdm
from helpfns import frame_to_bgrhsvlab, get_cubies
import numpy as np
from logisticmodel import log_model


#%%
from nxtsend import turn_cube

#%%
#methods = "sheet", "txt", "camera"
method = "camera"

if method == "sheet":
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRH493yWiJFM6gkZUN5TACSyGDMvLGIicTTLJXOrzLQeDhNfVXXjHUqAGfeDrhLbGmRRVjIug6HVL_J/pub?gid=0&single=true&output=csv', 
    header = None)

    def get_face_str(row_start, row_end, col_start, col_end): 
        face_table = df.iloc[row_start:row_end, col_start:col_end]
        face_list = face_table.values.tolist()
        face_str = ''.join([col for row in face_list for col in row])
        return face_str.lower()


    yellow_str = get_face_str(0,3,4,7)
    blue_str = get_face_str(4,7,0,3)
    red_str = get_face_str(4,7,4,7)
    green_str = get_face_str(4,7,8,11)
    orange_str = get_face_str(4,7,12,15)
    white_str = get_face_str(8,11,4,7)
    state = yellow_str + blue_str + red_str + green_str + orange_str + white_str

if method == "camera":
    takepix.takepics().show()
    
    faces_path = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Gitfolder/lego-nxt-cube-solver/Faces/'
    red_face = cv2.imread(faces_path + 'r4.png')
    orange_face = cv2.imread(faces_path + 'o4.png')
    green_face = cv2.imread(faces_path + 'g4.png')
    blue_face = cv2.imread(faces_path + 'b4.png')
    yellow_face = cv2.imread(faces_path + 'y4.png')
    white_face = cv2.imread(faces_path + 'w4.png')

    all_faces = [yellow_face, blue_face, red_face, green_face, orange_face, white_face]
    color_dict = {0: 'blue', 1: 'green', 2: 'orange', 3: 'red', 4: 'white', 5: 'yellow'}
    
    #with open('model1.pickle', 'rb') as handle:
    #    log_reg_model = pickle.load(handle)
    log_reg_model = log_model()
    
    all_pred_col = []
    for face in tqdm(all_faces): 
        dom_col_cubies = [np.array(frame_to_bgrhsvlab(x)) for x in get_cubies(face, False)]
        pred_cols = [color_dict[log_reg_model.predict(x.reshape(1, -1))[0]][0] for x in dom_col_cubies]
        all_pred_col.append(pred_cols)
    
        
    #add missing middle cubie
    col_order = ['y', 'b', 'r', 'g', 'o', 'w']
    for i, col_str in enumerate(col_order): 
        all_pred_col[i].insert(4, col_order[i])

    
    state = "".join([x for xs in all_pred_col for x in xs])

    #write state to txt file for doublechecking

    all_sides = ["".join(x) for x in all_pred_col]
    with open("state.txt", "w") as f_: 
        for side in all_sides: 
            f_.write(f"{side[0:3]}\n{side[3:6]}\n{side[6:9]}\n\n")

    #check that the txt file is correct, then press enter
    input("Check txt file for accuracy")
    method = "txt"

if method == "txt": 

    with open('state.txt') as f: 
        lines = f.readlines()

    state = ''.join(lines).replace('\n', '')

# %%
solution = utils.solve(state, 'Kociemba')
# %%
turn_cube.turn_list(solution, wait=True)

# %%
