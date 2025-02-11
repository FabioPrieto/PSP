import os
import openai
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from pydub import AudioSegment

# 🔐 Configuración con variables de entorno
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configurar OpenAI
openai.api_key = OPENAI_API_KEY

# 🎤 Función para manejar mensajes de voz
async def transcribe_voice(update: Update, context: CallbackContext):
    file = await update.message.voice.get_file()
    file_path = "audio.ogg"
    await file.download_to_drive(file_path)

    # Convertir OGG a WAV (Whisper solo acepta MP3, WAV, FLAC)
    audio = AudioSegment.from_file(file_path, format="ogg")
    wav_path = "audio.wav"
    audio.export(wav_path, format="wav")

    # Enviar audio a OpenAI Whisper
    with open(wav_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)

    # Enviar transcripción al usuario
    await update.message.reply_text(f"📝 Transcripción: {response['text']}")

    # Eliminar archivos temporales
    os.remove(file_path)
    os.remove(wav_path)

# 📌 Configuración del bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Manejar mensajes de voz
    app.add_handler(MessageHandler(filters.VOICE, transcribe_voice))

    print("🤖 Bot en ejecución...")
    app.run_polling()

if __name__ == "__main__":
    main()
