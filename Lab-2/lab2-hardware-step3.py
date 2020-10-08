import pi_emulator as pyEmulator
import time

#Create an object from temperature and display mod classes
temp = pyEmulator.tempMod()
disp = pyEmulator.dispMod()

#initialize disp
disp.init()

while(1):
    t = temp.readC()
    dispMsg = "Temp : " + str(t)
    disp.Print(dispMsg)
    time.sleep(1)