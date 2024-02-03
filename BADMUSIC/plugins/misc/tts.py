from pyrogram import Client, filters
from gtts import gTTS
from BADMUSIC import app


@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('ᴮᴬᴰ ᴬᵁᴰᴵᴼ.mp3')
    client.send_audio(message.chat.id, 'ᴮᴬᴰ ᴬᵁᴰᴵᴼ.mp3')

