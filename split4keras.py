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

take_pics.show(path=save_in, add_rand_num=True)

#%%
##split pictures into colour folders
image_list = []
for filename in glob.glob("C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Faces/Test/*.png"): 
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


