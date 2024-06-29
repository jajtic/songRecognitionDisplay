import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from screeninfo import get_monitors
import ast, os
import platform

root = tk.Tk()

# Function to kill the window
def kill_window(event=None):
    print("Pressed ESC; exiting")
    root.destroy()
    if os.path.exists("data.song"):
        os.remove("data.song")

def get_song_data():
    try:
        with open("data.song", "r") as f:
            song_data = f.read()
        return ast.literal_eval(song_data)
    except (SyntaxError, ValueError, FileNotFoundError) as e:
        print(f"Error reading song data: {e}")
        return {
            'title': 'Error',
            'artist': 'Error loading data',
            'album': 'The song might not be recognized yet',
            'year': "Check the data.song file if you're stuck here for some time",
            'album_art': 'album-cover-default.png'
        }

# Function to create the UI layout and display initial song info
def create_ui():
    global album_art_label, title_label, artist_label, album_label, year_label, album_art

    # Get the list of monitors
    monitors = get_monitors()

    # Select the monitor (0 MAIN, 1 SECONDARY)
    secondary_monitor = monitors[0]

    # Exit fullscreen with 'Esc' key
    root.bind_all("<Escape>", kill_window)

    # Set the background color
    root.configure(background='black')

    # Set the window geometry to the size of the secondary monitor
    root.geometry(f"{secondary_monitor.width}x{secondary_monitor.height}+{secondary_monitor.x}+{secondary_monitor.y}")

    # Platform-specific fullscreen settings
    if platform.system() == 'Linux':
        root.attributes("-fullscreen", True)
    else:
        root.overrideredirect(True)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    root.focus_set()
    root.update_idletasks()
    root.state("normal")

    # Create a frame to hold the content
    content_frame = Frame(root, bg='black')
    content_frame.pack(expand=True, pady=(0, 0))  # Adjust the padding value to move the content down

    # Create a subframe for the album art and text labels
    album_art_frame = Frame(content_frame, bg='black')
    album_art_frame.grid(row=0, column=0, padx=(100, 50), pady=20, sticky='n')  # Add padding to keep it in place

    text_frame = Frame(content_frame, bg='black')
    text_frame.grid(row=0, column=1, pady=20, sticky='n')

    # Add column weight to keep the album art fixed
    content_frame.grid_columnconfigure(0, weight=0)
    content_frame.grid_columnconfigure(1, weight=1)

    # Initialize labels without content
    album_art_label = Label(album_art_frame, bg='black')
    album_art_label.pack()

    title_label = Label(text_frame, fg='white', bg='black', font=('Helvetica', 36, "bold"))
    title_label.pack(pady=10, anchor='w')

    artist_label = Label(text_frame, fg='white', bg='black', font=('Helvetica', 30))
    artist_label.pack(pady=10, anchor='w')

    album_label = Label(text_frame, fg='white', bg='black', font=('Helvetica', 24))
    album_label.pack(pady=10, anchor='w')

    year_label = Label(text_frame, fg='white', bg='black', font=('Helvetica', 24))
    year_label.pack(pady=10, anchor='w')

    # Display initial song info
    display_song_info({
        'title': 'Please wait',
        'artist': 'Waiting for data',
        'album': 'Information should come up soon',
        'year': 'Make sure you have a microphone connected and that main.py is running',
        'album_art': 'album-cover-default.png'
    })

# Function to update the displayed song info
def display_song_info(song_info):
    global album_art

    # Load album art
    try:
        album_art = Image.open(song_info['album_art'])
        album_art = album_art.resize((300, 300))
        album_art = ImageTk.PhotoImage(album_art)
    except Exception as e:
        print(f"Error loading album art: {e}")
        album_art = None

    # Update album art
    if album_art:
        album_art_label.config(image=album_art)
    else:
        album_art_label.config(image='')

    # Update text labels
    title_label.config(text=song_info['title'])
    artist_label.config(text=song_info['artist'])
    album_label.config(text=song_info['album'])
    year_label.config(text=song_info['year'])

    # Schedule the next update
    root.after(5000, refresh_song_info)

# Function to refresh the song info
def refresh_song_info():
    song_info = get_song_data()
    display_song_info(song_info)

# Create the UI layout
create_ui()

# Display initial song info
display_song_info({
    'title': 'Please wait',
    'artist': 'Waiting for data',
    'album': 'Information should come up soon',
    'year': 'Make sure you have a microphone connected and that main.py is running',
    'album_art': 'album-cover-default.png'
})

# Run the Tkinter main loop
root.mainloop()
