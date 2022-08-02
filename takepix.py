#%%
import cv2
import random

class takepics: 
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.centercolor = (0,0,0)

        self.startcorner = 50
        self.cubesize = 300

        self.imgsave_num = 4
        self.imgsave_col = 'p'
        self.path = "C:/Users/Ayoola_PC/Documents/PythonScripts/Rubiks_cube/Gitfolder/lego-nxt-cube-solver/Faces/"
            
        #self.greenlines = False

    def show(self): 
        while True: 
            #cv2.namedWindow('Take Pics')
            _, frame = self.cam.read()
            frame = cv2.flip(frame, 1)
            k = cv2.waitKey(10) & 0xff

            if k == 27: 
                break
            elif k == ord('g'): 
                self.centercolor = (0,255,0)
                self.imgsave_col = 'g'
            elif k == ord('r'): 
                self.centercolor = (0,0,255)
                self.imgsave_col = 'r'
            elif k == ord('b'): 
                self.centercolor = (255,0,0)
                self.imgsave_col = 'b'
            elif k == ord('o'): 
                self.centercolor = (0,164,255)
                self.imgsave_col = 'o'
            elif k == ord('y'): 
                self.centercolor = (0,233,255)
                self.imgsave_col = 'y'
            elif k == ord('w'): 
                self.centercolor = (255,255,255)
                self.imgsave_col = 'w'
            elif k == 32:
                img_name = f'{self.path}/{self.imgsave_col}{self.imgsave_num}.png'
                cv2.imwrite(img_name, (frame[self.startcorner:self.startcorner+self.cubesize, self.startcorner:self.startcorner+self.cubesize, :]))
                cv2.imwrite(img_name, cv2.flip(cv2.imread(img_name), 1))
                print(f'{self.imgsave_col} photo taken')
            else:
                #if self.hlines:  
                self.drawlines(frame, self.cubesize, self.startcorner, self.centercolor)
                #cv2.imshow('Take Pics2', frame)
            
            cv2.imshow('Take Pics', frame)

        self.cam.release()
        cv2.destroyAllWindows()

    def drawlines(self, frame, cubesize, start_point, centercolor):
        cubecell = int(cubesize/3)

        for i in range(3 + 1):
            start_line = (start_point, start_point + i * cubecell)
            end_line = (start_point + cubesize, start_point + i * cubecell)
            cv2.line(frame, start_line, end_line, (0,0,0), 2)

        for i in range(3 + 1):
            start_line = (start_point + i * cubecell, start_point)
            end_line = (start_point + i * cubecell, start_point + cubesize)
            cv2.line(frame, start_line, end_line, (0,0,0), 2)

        cv2.line(frame, (cubecell+start_point,cubecell+start_point), (cubecell*2+start_point,cubecell+start_point), centercolor, 2)
        cv2.line(frame, (cubecell+start_point,cubecell+start_point), (cubecell+start_point,cubecell*2+start_point), centercolor, 2)
        cv2.line(frame, (cubecell+start_point,cubecell*2+start_point), (cubecell*2+start_point,cubecell*2+start_point), centercolor, 2)
        cv2.line(frame, (cubecell*2+start_point,cubecell*2+start_point), (cubecell*2+start_point,cubecell+start_point), centercolor, 2)

take_pics = takepics()
            
# %%
#take_pics.show()
# %%
