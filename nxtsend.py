#%%
#import nxt
import time
import nxt.locator
import nxt.motor 
import nxt.motcont
# %%
nxt1 = nxt.locator.find(name='1234')

#%%
nxt2 = nxt.locator.find(name='Lol')
# %%
nxt1_a = nxt.motor.Motor(nxt1, nxt.motor.Port(0))
nxt1_b = nxt.motor.Motor(nxt1, nxt.motor.Port(1))
nxt1_c = nxt.motor.Motor(nxt1, nxt.motor.Port(2))

#%%
nxt2_a = nxt.motor.Motor(nxt2, nxt.motor.Port(0))
nxt2_b = nxt.motor.Motor(nxt2, nxt.motor.Port(1))
nxt2_c = nxt.motor.Motor(nxt2, nxt.motor.Port(2))
# %%
class turnCube: 
    def __init__(self, nx1, nx2): 

        #assign the motors
        #[motor, nxtbrick (1 or 2), adjustment]
        self.Umotor = [nxt1_b, 1]
        self.Fmotor = [nxt1_a, 1]
        self.Lmotor = [nxt1_c, 1]
        self.Rmotor = [nxt2_c, 2]
        self.Bmotor = [nxt2_a, 2]
        self.Dmotor = [nxt2_b, 2]

        #default power
        self.power = 50 

        #set up motor control.rxe
        self.mc1 = nxt.motcont.MotCont(nx1)
        self.mc1.start()

        self.mc2 = nxt.motcont.MotCont(nx2)
        self.mc2.start()

        self.adjust = 3 #number of degrees to adjust each turn

        self.sleep_time = 1 #number of seconds to sleep between moves

        self.invert_list = ["U", "R", "B"] #motors that are turning backward


    def invert(self, move): 
        if len(move)==1: 
                move  = move + "'"
        elif len(move) == 2 and move[1]=="'":
            move = move[0]
        return move
    
    def turn(self, move, power=None, degrees = 90): 
        
        if power is None: 
            power = self.power

        #invert motors that are turning backward
        #invert_list = ["R"]
        if move[0] in self.invert_list: 
            move = self.invert(move)

        move_dict = {'U': self.Umotor, 
            'F': self.Fmotor, 
            'L': self.Lmotor, 
            'R': self.Rmotor, 
            'B': self.Bmotor, 
            'D': self.Dmotor}
        
        if len(move) == 1: 
            motor = move_dict[move]
            
            if motor[1] == 1: 
                self.mc1.cmd(ports=motor[0].port, power=power, tacholimit=degrees)
            elif motor[1] == 2: 
                self.mc2.cmd(ports=motor[0].port, power=power, tacholimit=degrees)

        elif len(move) == 2:
            motor = move_dict[move[0]]
            if move[1] == "'": 
                if motor[1] == 1: 
                    self.mc1.cmd(ports=motor[0].port, power=-power, tacholimit=90+self.adjust)
                elif motor[1] == 2: 
                    self.mc2.cmd(ports=motor[0].port, power=-power, tacholimit=90+self.adjust)

            elif move[1] == '2': 
                if motor[1] == 1: 
                    self.mc1.cmd(ports=motor[0].port, power=power, tacholimit=90+self.adjust)
                    while not self.mc1.is_ready(motor[0].port): 
                        time.sleep(0.1)
                    self.mc1.cmd(ports=motor[0].port, power=power, tacholimit=90+self.adjust)
                elif motor[1] == 2: 
                    self.mc2.cmd(ports=motor[0].port, power=power, tacholimit=90 +self.adjust)
                    while not self.mc2.is_ready(motor[0].port): 
                        time.sleep(0.1)
                    self.mc2.cmd(ports=motor[0].port, power=power, tacholimit=90 +self.adjust)
    
    def turn_list(self, moves, wait=False, sleep=False):
        for move in moves: 
            self.turn(str(move))
            if sleep: 
                time.sleep(self.sleep_time)
            if wait: 
                input("")
            
       
            


        


            


turn_cube = turnCube(nxt1, nxt2)
# %%
