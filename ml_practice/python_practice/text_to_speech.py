
# pip install gTTS pyttsx3
import os
import pyttsx3
from gtts import gTTS

# Function to convert text to speech using pyttsx3
def pyttsx3_convert(text, filename, voice_gender='male', voice_age='adult'):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (speed and volume)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Set voice
    voices = engine.getProperty('voices')
    
    # Select voice based on gender
    if voice_gender == 'male':
        engine.setProperty('voice', voices[0].id)  # Male voice (typically)
    elif voice_gender == 'female':
        engine.setProperty('voice', voices[1].id)  # Female voice (typically)
    
    # Save the speech to a file
    engine.save_to_file(text, filename)
    engine.runAndWait()

# Function to convert text to speech using Google Text-to-Speech (gTTS)
def gtts_convert(text, filename, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(filename)

# Create the folder if it does not exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Main function to run the program
def convert_text_to_speech(text, voice_type='gtts', voice_gender='male', voice_age='adult'):
    folder_name = "generated_speech"
    create_folder(folder_name)
    
    # Generate the filename based on voice settings
    filename = os.path.join(folder_name, f"output_{voice_gender}_{voice_age}.mp3")

    if voice_type == 'gtts':
        # Google TTS
        gtts_convert(text, filename)
    elif voice_type == 'pyttsx3':
        # pyttsx3 TTS
        pyttsx3_convert(text, filename, voice_gender, voice_age)
    else:
        print("Invalid voice type. Please choose 'gtts' or 'pyttsx3'.")

    print(f"Speech saved to {filename}")

# Example usage
if __name__ == "__main__":
    text = ''' hello
'''
    convert_text_to_speech(text, voice_type='pyttsx3', voice_gender='male', voice_age='adult')  # Using Google TTS with male adult voice
