import pygame
import requests

pygame.mixer.init()

api_base_url = 'http://127.0.0.1:5000/'
response = requests.get(api_base_url)

if response.status_code == 200:
	file_from_api = response.text.strip()

	audio_file_path = f'./audios/{file_from_api}.mp3'
	pygame.mixer.music.load(audio_file_path)

	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy():
		pass

else:
    print("Failed to retrieve file name from the API.")