import os
from google.cloud import speech_v1
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import soundfile as sf
import io
import subprocess
import tempfile
import nest_asyncio
import logging
import time

# Enable nested event loops
nest_asyncio.apply()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Initialize Google Cloud client
client = speech_v1.SpeechClient()

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ogg_file = None
    wav_filename = None

    try:
        # Get voice message
        voice = await update.message.voice.get_file()

        # Create temporary files
        ogg_file = tempfile.NamedTemporaryFile(suffix='.ogg', delete=False)
        # Download voice message
        await voice.download_to_drive(ogg_file.name)
        ogg_file.close()  # Close the file before ffmpeg uses it

        # Create temporary WAV file name
        wav_filename = ogg_file.name[:-4] + '.wav'

        # Convert OGG to WAV using ffmpeg
        process = subprocess.run([
            'ffmpeg', '-i', ogg_file.name,
            '-acodec', 'pcm_s16le',
            '-ar', '48000',
            '-ac', '1',
            wav_filename
        ], check=True)

        # Read the WAV file
        with open(wav_filename, 'rb') as wav_file:
            audio_content = wav_file.read()

        # Prepare audio for Google Speech-to-Text
        audio = speech_v1.RecognitionAudio(content=audio_content)

        # Configure recognition
        config = speech_v1.RecognitionConfig(
            encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            language_code="es-ES",
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
        logging.error(f"Error in handle_voice: {str(e)}", exc_info=True)
        await update.message.reply_text(f"❌ Error processing voice message: {str(e)}")

    finally:
        # Clean up temporary files
        try:
            if ogg_file and os.path.exists(ogg_file.name):
                os.unlink(ogg_file.name)
            if wav_filename and os.path.exists(wav_filename):
                os.unlink(wav_filename)
        except Exception as e:
            logging.warning(f"Error cleaning up temporary files: {str(e)}")

def main():
    try:
        # Create application
        app = Application.builder().token(TELEGRAM_TOKEN).build()

        # Add handler for voice messages
        app.add_handler(MessageHandler(filters.VOICE, handle_voice))

        # Start bot
        print("🤖 Bot is running...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        logging.error(f"Error in main: {str(e)}", exc_info=True)
        raise

if __name__ == '__main__':
    main()

# Created/Modified files during execution:
# - Temporary .ogg and .wav files (automatically cleaned up after processing)