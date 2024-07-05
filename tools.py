import pyaudio, os, requests
import wave
from shazamio import Shazam

def record_audio(duration):
    # Set parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = duration
    WAVE_OUTPUT_FILENAME = "mic_output.wav"

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open audio stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=1024)  # Adjust buffer size as needed

    print("* Recording...")

    frames = []  # Store audio data

    # Record audio for the specified duration
    for _ in range(int(RATE / 1024 * RECORD_SECONDS)):
        data = stream.read(1024)
        frames.append(data)

    print("* Done recording")

    # Close the stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save recorded audio to a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Recording saved as {WAVE_OUTPUT_FILENAME}")

def download_album_art(img_url):
    response = requests.get(img_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary write mode
        with open('album-cover.png', 'wb') as file:
            # Write the content of the response to the file
            file.write(response.content)
        print("Image downloaded and saved as album-cover.png")
    else:
        print("Failed to retrieve the image - default will be used")

async def detect():
    shazam = Shazam()
    out = await shazam.recognize("mic_output.wav")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        title = out['track']['title']
        artist = out['track']['subtitle']
        album = next((item for item in out['track']['sections'][0]['metadata'] if item["title"] == "Album"), {}).get('text', 'Unknown')
        year = next((item for item in out['track']['sections'][0]['metadata'] if item["title"] == "Released"), {}).get('text', 'Unknown')
        album_cover_url = out['track']['images']['coverart']
        song_data = {"title": title, "artist": artist, "album": album, "year": year, "album_art": "album-cover.png"}
        with open("data.song", "w") as f:
            f.write(str(song_data))
        download_album_art(album_cover_url)
        print(f"Title: {title}\nArtist: {artist}\nAlbum: {album}\nYear: {year}\nAlbum cover URL: {album_cover_url}")
        os.remove("mic_output.wav")
    except:
        """ UNCOMMENT THE FOLLOWING LINES IF YOU WANT IT TO SAY UNKNOWN AS SOON AS IT FAILS TO DETECT A SONG (OTHERWISE THE TITLE OF THE PREVIOUSLY PLAYING SONG WILL STAY)
        with open("data.song", "w") as f:
            f.write(str("{'title': 'Unknown', 'artist': 'Unknown', 'album': 'Unknown', 'year': 'Unknown', 'album_art': 'album-cover-default.png'}"))
        """
        print("Could not recognize track")
        os.remove("mic_output.wav")
    