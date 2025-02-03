import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")
        
        pygame.mixer.init()
        
        self.current_song = ""
        
        self.label = tk.Label(root, text="No song selected", wraplength=250)
        self.label.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)
        
        self.load_button = tk.Button(root, text="Load Song", command=self.load_music)
        self.load_button.pack(pady=5)
        
    def load_music(self):
        self.current_song = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if self.current_song:
            self.label.config(text=self.current_song.split("/")[-1])
    
    def play_music(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
