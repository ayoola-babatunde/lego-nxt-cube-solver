#%% 
import cv2


cubecolor = (0,0,0)
cubelineSize = 2
cubesize = 300
startcorner = 50

def drawCube(img, cubesize, start_point, centercolor=cubecolor): # start_poing (100, 100)
    cubecell = int(cubesize / 3)
    # draw horizontal lines first
    for i in range(3 + 1):
        start_line = (start_point, start_point + i * cubecell)
        end_line = (start_point + cubesize, start_point + i * cubecell)
        cv2.line(img, start_line, end_line, cubecolor, 2)
    
    for i in range(3 + 1):
        start_line = (start_point + i * cubecell, start_point)
        end_line = (start_point + i * cubecell, start_point + cubesize)
        cv2.line(img, start_line, end_line, cubecolor, cubelineSize)

    cv2.line(img, (cubecell+start_point,cubecell+start_point), (cubecell*2+start_point,cubecell+start_point), centercolor, cubelineSize)
    cv2.line(img, (cubecell+start_point,cubecell+start_point), (cubecell+start_point,cubecell*2+start_point), centercolor, cubelineSize)
    cv2.line(img, (cubecell+start_point,cubecell*2+start_point), (cubecell*2+start_point,cubecell*2+start_point), centercolor, cubelineSize)
    cv2.line(img, (cubecell*2+start_point,cubecell*2+start_point), (cubecell*2+start_point,cubecell+start_point), centercolor, cubelineSize)


    return img



cv2.namedWindow("test")
cam = cv2.VideoCapture(0)

if cam.isOpened():  
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
else: 
    ret = False

img_counter = 0

while ret:
    cv2.imshow('test', frame)
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    #if not ret:
    #    print("failed to grab frame")
    #    break

    #frame  = drawCube(frame,cubesize,startcorner,cubecolor)

    cv2.imshow("test", frame)

    k = cv2.waitKey(10) & 0xFF

    
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == ord('g'): 
        print('g pressed')
        #cv2.line(frame, (0,0), (20,20), (45,200,45), 2)
        frame = drawCube(frame,cubesize,startcorner,(45,200,45))
        
        cv2.imshow("test", frame) 
        k = cv2.waitKey(0)
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame[startcorner:startcorner+cubesize, startcorner:startcorner+cubesize, :])
        print("{} written!".format(img_name))
        img_counter += 1
    

cam.release()

cv2.destroyAllWindows()
# %%
