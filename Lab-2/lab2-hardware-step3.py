import my_pi_emulator_1 as pyEmu
import time

#Create an object from temperature and display mod classes
temp = pyEmu.tempMod()
disp = pyEmu.dispMod()

#initialize disp
disp.init()

while(1):
    t = temp.readC()
    dispMsg = "Temp : " + str(t)
    disp.Print(dispMsg)
    time.sleep(1)