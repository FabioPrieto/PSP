import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from pydub import AudioSegment
import anthropic

# Environment variables configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Configure Claude client
claude = anthropic.Client(api_key=CLAUDE_API_KEY)

# Handle voice messages
async def transcribe_voice(update: Update, context: CallbackContext):
    try:
        file = await update.message.voice.get_file()
        file_path = "audio.ogg"
        await file.download_to_drive(file_path)

        # Convert OGG to WAV
        audio = AudioSegment.from_file(file_path, format="ogg")
        wav_path = "audio.wav"
        audio.export(wav_path, format="wav")

        # Send audio to Claude for transcription
        with open(wav_path, "rb") as audio_file:
            # Create a message with the audio file
            message = claude.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please transcribe this audio file:"
                        },
                        {
                            "type": "audio",
                            "source": {
                                "type": "base64",
                                "data": audio_file.read()
                            }
                        }
                    ]
                }]
            )

        # Send transcription to user
        transcription = message.content[0].text
        await update.message.reply_text(f"📝 Transcription: {transcription}")

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
    finally:
        # Clean up temporary files
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)

# Bot configuration
def main():
    app = Application.builder().token(TOKEN).build()

    # Handle voice messages
    app.add_handler(MessageHandler(filters.VOICE, transcribe_voice))

    print("🤖 Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()

# Created/Modified files during execution:
# - audio.ogg (temporary)
# - audio.wav (temporary)