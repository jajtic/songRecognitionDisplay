import asyncio, os
from tools import record_audio, detect

while True:
    record_audio(12)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(detect())