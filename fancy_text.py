from art import *
import time

string = "Hello, world!"
ascii_text = text2art(string, font='dancing_font')
for char in ascii_text:
    
    print(char, end= '',flush=True)
    time.sleep(0.001)
