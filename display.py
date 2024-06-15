import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
from screeninfo import get_monitors
import ast, os

root = tk.Tk()

# Function to kill the window
def kill_window():
    root.quit()
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
    secondary_monitor = monitors[1]

    # Exit fullscreen with 'Esc' key
    root.bind("<Escape>", lambda e: kill_window())

    # Set the background color
    root.configure(background='black')

    # Set the window geometry to the size of the secondary monitor
    root.geometry(f"{secondary_monitor.width}x{secondary_monitor.height}+{secondary_monitor.x}+{secondary_monitor.y}")

    # Manually maximize the window without borders
    root.overrideredirect(True)
    root.update_idletasks()
    root.state('zoomed')

    # Create a frame to hold the content
    content_frame = Frame(root, bg='black')
    content_frame.pack(pady=50)  # Adjust the padding value to move the content down

    # Initialize labels without content
    album_art_label = Label(content_frame, bg='black')
    album_art_label.pack(pady=20)
    title_label = Label(content_frame, fg='white', bg='black', font=('Helvetica', 32, "bold"))
    title_label.pack(pady=10)
    artist_label = Label(content_frame, fg='white', bg='black', font=('Helvetica', 26))
    artist_label.pack(pady=10)
    album_label = Label(content_frame, fg='white', bg='black', font=('Helvetica', 20))
    album_label.pack(pady=10)
    year_label = Label(content_frame, fg='white', bg='black', font=('Helvetica', 20))
    year_label.pack(pady=10)

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