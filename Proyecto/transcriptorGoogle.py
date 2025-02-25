import os
from google.cloud import speech_v1
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from pydub import AudioSegment
import io

# Environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Initialize Google Cloud client
client = speech_v1.SpeechClient()

async def handle_voice(update: Update, context: CallbackContext):
    try:
        # Get voice message
        voice = await update.message.voice.get_file()

        # Download voice message
        voice_file = io.BytesIO()
        await voice.download_to_memory(voice_file)

        # Convert to WAV using pydub
        audio = AudioSegment.from_ogg(voice_file)
        wav_io = io.BytesIO()
        audio.export(wav_io, format='wav')
        wav_io.seek(0)

        # Prepare audio content for Google Speech-to-Text
        audio_content = wav_io.read()
        audio = speech_v1.RecognitionAudio(content=audio_content)

        # Configure recognition
        config = speech_v1.RecognitionConfig(
            encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,  # Telegram voice messages are usually 48kHz
            language_code="es-ES",    # Change this to your preferred language
            enable_automatic_punctuation=True,
        )

        # Perform transcription
        await update.message.reply_text("🎯 Processing your voice message...")
        response = client.recognize(config=config, audio=audio)

        # Send transcription
        for result in response.results:
            transcript = result.alternatives[0].transcript
            await update.message.reply_text(f"📝 Transcription:\n{transcript}")

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    # Create application
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handler for voice messages
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    # Start bot
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

# Created/Modified files during execution:
# - No permanent files created (all processing done in memory)