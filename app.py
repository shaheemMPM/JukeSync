import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Load the audio file
audio_file_path = '1.mp3'  # Replace with your audio file path
pygame.mixer.music.load(audio_file_path)

# Play the audio
pygame.mixer.music.play()

# Keep the program running to allow audio to play
while pygame.mixer.music.get_busy():
    pass
