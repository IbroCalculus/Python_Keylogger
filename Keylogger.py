from pynput.mouse import Controller as MouseCtrl
from pynput.keyboard import Controller as KeyCtrl
from pynput.keyboard import Listener as KeyListener
from pynput.mouse import Listener as MouseListener
from time import sleep

'''
    THINGS PYNPUT MODULE CAN DO
    1- Controlling the mouse
    2- Controlling the keyboard
    3- Listening to the mouse events
    4- Listening to the keypboard events
'''
#NB: Mouse and Keyboard cannot be controlled simultaneously. Only one at a time.

#=================== CONTROL THE MOUSE VIA CODE =======================
def ControlMouse():
    thisMouse = MouseCtrl()
    thisMouse.position = (10, 20)        #x,y
    print("Position set")
sleep(3)
#ControlMouse()

#================== CONTROL THE KEYBOARD OR TYPE VIA CODE ==================
def ControlKeyboard():
    thisKeyboard = KeyCtrl()
    thisKeyboard.type("This is it")
sleep(3)
#ControlKeyboard()

#====================== LISTEN FOR KEYBOARD ACTIVITIES =======================
def ListenForKeyboard():
    def logKeyData(key):        #key is of variable type keycode
        keyString = str(key)                # This output string in a format like: 'r', 'a', '4' etc
        with open("Keylogger.txt", 'a') as k:
            keyString = keyString.replace("'", "")          #Replace the single quote with nothing
            k.write(keyString)

    with KeyListener(on_press=logKeyData) as l:
        l.join()
#ListenForKeyboard()

#==================== LISTEN FOR MOUSE POSITION VIA CODE =====================
def ListenForMouse():
    def logMousePos(x,y):
        print(f'Current Pos: {x}, {y}')

    with MouseListener(on_move=logMousePos) as m:
        m.join()
#ListenForMouse()
