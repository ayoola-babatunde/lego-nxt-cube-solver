#%%
from rubik_solver import utils
import pandas as pd


#%%
from nxtsend import turn_cube

#%%
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


# %%
with open('state.txt') as f: 
    lines = f.readlines()

state = ''.join(lines).replace('\n', '')
# %%
solution = utils.solve(state, 'Kociemba')
# %%
turn_cube.execute(solution)

# %%
