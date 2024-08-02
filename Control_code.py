import pygame
import time
import termcolor
import pyfiglet
x = .03
pygame.init()
pygame.joystick.init()


def joy_G_Init():
    init = pygame.joystick.get_init()
    print(
        f"The State Of Initialization Is : ({init})")
    time.sleep(x)


def num_Of_Joy():
    global num
    num = pygame.joystick.get_count()
    print(f"{num} Joystick Connected")
    time.sleep(x)


def joy_Name():
    name = joystick.get_name()
    print(f"Joystick Name Is : {name}")
    time.sleep(x)


def joy_Id():
    Id = joystick.get_id()
    print(f"Joystick Id : {Id}")
    time.sleep(x)


def joy_Num_Axes():
    global Axess
    Axess = joystick.get_numaxes()
    print(f"Number Of Axes: {Axess}")
    time.sleep(x)


def joy_Num_Buttons():
    global Buttons
    Buttons = joystick.get_numbuttons()
    print(f"Number Of Buttons: {Buttons}")
    time.sleep(x)


def Axes():
    for i in range(Axess):
        Ss = joystick.get_axis(i)
        print(f"Axis {i} => {Ss}")
        time.sleep(x)


def joy_Num_Balls():
    Balls = joystick.get_numballs()
    print(f"Number Of Balls : {Balls}")


def Buton():
    for i in range(Buttons):
        bt = bool(joystick.get_button(i))
        print(f"Button {i:02} => {bt}")
        time.sleep(x)


def joy_Num_Hats():
    global hats
    hats = joystick.get_numhats()
    print(f"Number Of Hats : {hats}")


def hat():
    for i in range(hats):
        ht = joystick.get_hat(i)
        print(f"Hat {i} => {ht}")
        time.sleep(x)


print("="*40)
time.sleep(x)
print(termcolor.colored(pyfiglet.figlet_format("ROV"), color="blue"))
print("="*40)
time.sleep(x)
num_Of_Joy()

if num == 0:
    pygame.joystick.quit()
    joy_G_Init()
    print("No Joystick Connected Pls Check cable connection")
    print("="*40)
    exit()

joy_G_Init()
print("="*40)


for i in range(num):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print("/"*40)
    joy = f" joystick num {i+1} "
    joy = joy.center(40, "/")
    print(f"{joy}")
    print("/"*40)
    print("="*40)
    time.sleep(x)
    joy_Name()
    time.sleep(x)
    joy_Id()
    time.sleep(x)
    print("="*40)

    joy_Num_Axes()
    time.sleep(x)
    joy_Num_Buttons()
    time.sleep(x)
    joy_Num_Balls()
    time.sleep(x)
    joy_Num_Hats()
    time.sleep(x)

    print("="*40)
    time.sleep(x)
    Axes()
    time.sleep(x)
    print("="*40)
    time.sleep(x)
    Buton()
    time.sleep(x)
    print("="*40)
    time.sleep(x)
    hat()
    time.sleep(x)
    print("="*40)
    time.sleep(x)
while (1):
    Axes()
    time.sleep(x)
    Buton()
    time.sleep(x)
    pygame.event.pump()
