# Libraries
import datetime
import os
from pynput import keyboard
from pynput import mouse
import time

class Logger:
    """Simple class to create log events.
    Methods:
        init_file(): Create the file if it doesn't exist and overwrite if renew equals True, or append if renew equals False.
        log(event: str): Oppen the file and write the return of time followed by the given event.
        delete_log(): Removes the log file if it exists.
    """
    def __init__(self, filename: str, time: callable=datetime.datetime.now, renew: bool=False):
        """
        Args:
            filename (str): The name of the file to store the logs.
            time (callable, optional=datetime.datetime.now): A function to get the current time (written at the start of a log and at every event)
            renew (bool, optional=False): Renew the file every time, if False append to the existent file if it exists, if it doens't create it
        """
        self.filename = filename
        self.time = time
        self.renew = renew

        self.init_file()

    def init_file(self):
        """
        """
        if "/" in self.filename: # if "/" in filename means that if it's a path

            path = self.filename.split("/") # Split the path by / to iterate through

            for e, i in enumerate(path): # Iterate through the directory
                
                if e == len(path) - 1: break # If we are in the last element when split("/"), which means the filename break because isn't a folder
                
                if not os.path.isdir(i): os.mkdir(i) # If isn't the filename (last element) create folder if it doesn't exist

        with open(self.filename, "a" if not self.renew else "w") as file: # Append to the file or overwrite the file with the time
            file.write(f"--- [{self.time()}] ---\n") # Write time func 

    def log(self, event: str):
        """
        """
        print(event)
        with open(self.filename, "a") as file: # Open file to append
            file.write(f"[{self.time()}] {event}\n") # Write the time func and the given text

    def delete_log(self):
        """
        """
        if os._exists(self.filename): os.remove(self.filename) # If the file exists remove it

class KeyLogger(Logger):
    """
    """
    def __init__(self, filename: str, time: callable=datetime.datetime.now, renew: bool=False):
        super().__init__(filename, time=time, renew=renew)

    def on_press(self, key, escape_key=None):
        self.log(f"Pressed {key}")

        if key == escape_key:
            print(f"{self} stopped with {key}")
            return False

    def on_release(self, key, escape_key=keyboard.Key.esc):
        self.log(f"Released {key}")
        
        if key == escape_key:
            print(f"{self} stopped with {key}")
            return False

    def init_logging(self, on_press: callable=None, on_release: callable=None, on_press_escape_key=None, on_release_escape_key=keyboard.Key.esc):
        on_press = self.on_press if on_press == None else on_press
        on_release = self.on_release if on_release == None else on_release

        if isinstance(on_press_escape_key, str):
            on_press_escape_key = f"'{on_press_escape_key}'"
        if isinstance(on_release_escape_key, str):
            on_release_escape_key = f"'{on_release_escape_key}'"

        with keyboard.Listener(
                on_press=lambda key: on_press(str(key) if isinstance(on_press_escape_key, str) else key, on_press_escape_key),
                on_release=lambda key: on_release(str(key) if isinstance(on_release_escape_key, str) else key, on_release_escape_key)) as listener:
            
            listener.join()

class MouseLogger(Logger):
    """
    """
    def __init__(self, filename: str, time: callable=datetime.datetime.now, renew: bool=False):
        super().__init__(filename, time=time, renew=renew)

    def on_move(self, x, y):
        self.log(f"Move {(x, y)}")

        """if event == escape_key:
            print(f"{self} stopped with {event}")
            return False"""

    def on_click(self, x: int, y: int, button, pressed: int):
        self.log(f"Click {(x, y, button, pressed)}")
        
        """if event == escape_key:
            print(f"{self} stopped with {event}")
            return False"""

    def on_scroll(self, x, y, dx, dy):
        self.log(f"Scroll {(x, y, dx, dy)}")
        
        """if event == escape_key:
            print(f"{self} stopped with {event}")
            return False"""

    def init_logging(self, on_move: callable=None, on_click: callable=None, on_scroll=None):
        on_move = self.on_move if on_move == None else on_move
        on_click = self.on_click if on_click == None else on_click
        on_scroll = self.on_scroll if on_scroll == None else on_scroll

        with mouse.Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll) as listener:
            listener.join()

