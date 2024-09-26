import tkinter as tk
from gtts import gTTS
import pygame

def text_to_speech():
    text = entry.get() 
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            continue

# GUI
root = tk.Tk()
root.title("Text to Speech")

label = tk.Label(root, text="Enter text:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=20)

button = tk.Button(root, text="Convert to Speech", command=text_to_speech)
button.pack(pady=20)

root.mainloop()
