from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    print(f"Text converted to speech. Saved as {filename}")

if __name__ == "__main__":
    user_text = input("Enter the text you want to convert to speech: ")
    language = input("Enter the language (e.g., 'en' for English, 'fr' for French): ")
    filename = input("Enter the filename for the output speech file (without extension): ") + '.mp3'

    text_to_speech(user_text, language=language, filename=filename)

    print("Enjoy your speech! 🎉")