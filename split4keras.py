#%%
import glob
import cv2
from takepix import take_pics
from helpfns import get_cubies
import random
from tqdm import tqdm
# %%
##take pictures of sides
save_in = "C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Gitfolder/lego-nxt-cube-solver/Faces/Test/"

#%%
take_pics.show(path=save_in, add_rand_num=True)

#%%
##split pictures into colour folders
#get path for faces pics
image_list = []
for filename in glob.glob("C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Gitfolder/lego-nxt-cube-solver/Faces/Test/*.png"): 
    image_list.append(filename)

# %%
#split into cubies
for image in tqdm(image_list): 
    #print(image)
    cubies = get_cubies(cv2.imread(image), False)
    for cubie in cubies: 
        cv2.imwrite(f'{save_in+"Cubies3/"}/{random.randint(1,100000)}.png', cubie)
    #get_cubies(frame)

    
# %%
#get path for cubie pics
all_cubies = []
for cubie in glob.glob("C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Gitfolder/lego-nxt-cube-solver/Faces/Test/Cubies3/*.png"): 
    all_cubies.append(cubie)
# %%
#sort cubies into folders
for cubie in tqdm(all_cubies): 
    image = cv2.imread(cubie)
    cv2.imshow('', image)
    k = cv2.waitKey()

    if k == ord('g'): 
        cv2.imwrite(f'{save_in}/Cubies3/green3/{random.randint(1,100000)}.png', image)
    if k == ord('b'): 
        cv2.imwrite(f'{save_in}/Cubies3/blue3/{random.randint(1,100000)}.png', image)
    if k == ord('o'): 
        cv2.imwrite(f'{save_in}/Cubies3/orange3/{random.randint(1,100000)}.png', image)
    if k == ord('r'): 
        cv2.imwrite(f'{save_in}/Cubies3/red3/{random.randint(1,100000)}.png', image)
    if k == ord('w'): 
        cv2.imwrite(f'{save_in}/Cubies3/white3/{random.randint(1,100000)}.png', image)
    if k == ord('y'): 
        cv2.imwrite(f'{save_in}/Cubies3/yellow3/{random.randint(1,100000)}.png', image)
    if k == 27: 
        break
cv2.destroyAllWindows()



# %%
