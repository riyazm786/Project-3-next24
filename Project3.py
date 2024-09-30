pip install lyricsgenius
pip install tkinter
import tkinter as tk
from tkinter import messagebox, scrolledtext
import lyricsgenius

# Genius API Setup (Replace with your own API key)
GENIUS_API_KEY = 'your_genius_api_key'
genius = lyricsgenius.Genius(GENIUS_API_KEY)

# Function to fetch lyrics
def fetch_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()

    if artist and song:
        try:
            # Searching for the song
            song_lyrics = genius.search_song(song, artist)
            if song_lyrics:
                lyrics_display.delete(1.0, tk.END)
                lyrics_display.insert(tk.END, song_lyrics.lyrics)
            else:
                messagebox.showerror("Error", "Lyrics not found for the given song and artist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")

# Create the main window
window = tk.Tk()
window.title("Lyrics Extractor")
window.geometry("500x400")

# Song Label and Entry
song_label = tk.Label(window, text="Song Name:")
song_label.pack(pady=5)
song_entry = tk.Entry(window, width=40)
song_entry.pack(pady=5)

# Artist Label and Entry
artist_label = tk.Label(window, text="Artist Name:")
artist_label.pack(pady=5)
artist_entry = tk.Entry(window, width=40)
artist_entry.pack(pady=5)

# Fetch Button
fetch_button = tk.Button(window, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.pack(pady=10)

# Lyrics Display
lyrics_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15)
lyrics_display.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
