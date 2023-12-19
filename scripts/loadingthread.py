import threading
import time
import sys

class LoadingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.stop_flag = False
        self.frames = [
			"⣾",
			"⣽",
			"⣻",
			"⢿",
			"⡿",
			"⣟",
			"⣯",
			"⣷"
		]

    def run(self):
        #frames = ["◜", "◠", "◝", "◞", "◡", "◟"]
        index = 0
        while not self.stop_flag:
            print(f"Listening {self.frames[index]}", end="\r", flush=True)
            time.sleep(0.064)
            print("   ", end="\r")
            index -= 1
            index %= len(self.frames)

def loading():
    frames = [
			"⣾",
			"⣽",
			"⣻",
			"⢿",
			"⡿",
			"⣟",
			"⣯",
			"⣷"]
    
    index = 0        
    while True:
        print(f"Listening {frames[index]}", end="\r", flush=True)
        time.sleep(0.064)
        print("   ", end="\r")
        index -= 1
        index %= len(frames)