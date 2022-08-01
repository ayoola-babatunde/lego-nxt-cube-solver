# %%
from rubik_solver import utils
import cv2
import numpy as np
from helpfns import bgr2lab, ciede2000, show_color
import matplotlib.pyplot as plt
from takepix import take_pics

#%%
from nxtsend import turn_cube

#%%
#take_pics.show()

# %%
faces_path = 'C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/'
red_face = cv2.imread(faces_path + 'r3.png')
orange_face = cv2.imread(faces_path + 'o3.png')
green_face = cv2.imread(faces_path + 'g3.png')
blue_face = cv2.imread(faces_path + 'b3.png')
yellow_face = cv2.imread(faces_path + 'y3.png')
white_face = cv2.imread(faces_path + 'w3.png')

all_faces = [yellow_face, blue_face, red_face, green_face, orange_face, white_face]
all_colors = ['y', 'b', 'r', 'g', 'o', 'w']


#%%
def get_dominant_color(roi, ncolor =  1):
    """
    Get dominant color from a certain region of interest.

    :param roi: The image list.
    :returns: tuple
    """
    #average = roi.mean(axis=0).mean(axis=0)
    pixels = np.float32(roi.reshape(-1, 3))

    n_colors = ncolor
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    #dominant = palette[np.argmax(counts)]
    #return np.array(tuple(dominant))
    return palette, counts


#%%
def get_cubies(face):
    w_, l_ = face.shape[:2] #width, length

    
    cubie1 = face[:int(w_/3),               :int(l_/3),             :] #1 is top left, 9 is bottom right
    cubie2 = face[:int(w_/3),               int(l_/3):int(2*l_/3),  :]
    cubie3 = face[:int(w_/3),               int(2*l_/3):int(l_),    :]
    cubie4 = face[int(w_/3):int(2*w_/3),    :int(l_/3),             :]
    cubie5 = face[int(w_/3):int(2*w_/3),    int(l_/3):int(2*l_/3),  :]
    cubie6 = face[int(w_/3):int(2*w_/3),    int(2*l_/3):int(l_),    :]
    cubie7 = face[int(2*w_/3):int(w_),      :int(l_/3),             :]
    cubie8 = face[int(2*w_/3):int(w_),      int(l_/3):int(2*l_/3),  :]
    cubie9 = face[int(2*w_/3):int(w_),      int(2*l_/3):int(l_),    :]
    
    #return get_color(cubie1), get_color(cubie2), get_color(cubie3), get_color(cubie4), get_color(cubie5), get_color(cubie6), get_color(cubie7), get_color(cubie8), get_color(cubie9)

    return cubie1, cubie2, cubie3, cubie4, cubie5, cubie6, cubie7, cubie8, cubie9

#%%
def dom_col2(pixels): 
    n_colors = 1
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    return palette, counts
# %%

def bincount_app(a):
    a2D = a.reshape(-1,a.shape[-1])
    col_range = (256, 256, 256) # generically : a2D.max(0)+1
    a1D = np.ravel_multi_index(a2D.T, col_range)
    return np.unravel_index(np.bincount(a1D).argmax(), col_range)
# %%

#%%
def calibrate2(face):
    'Returns dominant color of middle cubie in brg'
    middlecubie = get_cubies(face)[4] 
    domcolor = get_dominant_color(middlecubie)
    return domcolor

def calibrate(face):
    'Returns dominant color of middle cubie in brg'
    middlecubie = get_cubies(face)[4] 
    domcolor = bincount_app(middlecubie)
    return np.array(domcolor)

# %%

#standard colour definitions
the_red = calibrate(red_face)
the_orange = calibrate(orange_face)
the_green = calibrate(green_face)
the_blue = calibrate(blue_face)
the_yellow = calibrate(yellow_face)
the_white = calibrate(white_face)

the_colors = [the_red, the_orange, the_green, the_blue, the_yellow, the_white]

#%%
def get_distance(col1, col2): 
    return ciede2000(bgr2lab(col1), bgr2lab(col2))


# %%
def get_color(cubie): 
    #b = np.mean(cubie[:, :, 0])
    #g = np.mean(cubie[:, :, 1])
    #r = np.mean(cubie[:, :, 2])

    #avg_color = np.array([r, g, b])

    distances =  [get_distance(bincount_app(cubie),the_red), 
                get_distance(bincount_app(cubie),the_orange), 
                get_distance(bincount_app(cubie),the_green), 
                get_distance(bincount_app(cubie),the_blue), 
                get_distance(bincount_app(cubie),the_yellow), 
                get_distance(bincount_app(cubie),the_white)]

    min_index = distances.index(min(distances))
    if min_index == 0: 
        return 'r'
    if min_index == 1: 
        return 'o'
    if min_index == 2: 
        return 'g'
    if min_index == 3: 
        return 'b'
    if min_index == 4: 
        return 'y'
    if min_index == 5: 
        return 'w'
    

def get_state(): 
    state_list = []
    for face in all_faces: 
        state_list = state_list + [get_color(cubie) for cubie in get_cubies(face)]
    state = ''.join(state_list)
    return state

# %%
cube_state = get_state()

#%%
solution = utils.solve(cube_state, 'Kociemba')

#%%
#turn_cube.execute(solution)



