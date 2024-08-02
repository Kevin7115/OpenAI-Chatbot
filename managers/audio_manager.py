import pygame
import os
from rich import print

# Documentation: https://www.pygame.org/docs/
# or, search something like "playing audio pygame"

class AudioManager:

    def __init__(self):
        # Use higher frequency to prevent audio glitching noises
        # Use higher buffer because why not (default is 512)
        pygame.mixer.init(frequency=48000, buffer=1024)
        # pygame.init()
        # pygame.display.set_mode((200,100)) 

    def play_audio(self, file_path, sleep_during_playback=True, delete_file=False, play_using_music=True):
        """
        Parameters:
        file_path (str): path to the audio file
        sleep_during_playback (bool): means program will wait for length of audio file before returning
        delete_file (bool): means file is deleted after playback (note that this shouldn't be used for multithreaded function calls)
        play_using_music (bool): means it will use Pygame Music, if false then uses pygame Sound instead
        """
        print(f"Playing file with pygame: {file_path}")
        if not pygame.mixer.get_init(): # Reinitialize mixer if needed
            pygame.mixer.init(frequency=48000, buffer=1024) 
        if play_using_music:
            pygame.mixer.Sound(file_path).play()
        else:
            # Pygame Sound lets you play multiple sounds simultaneously
            pygame_sound = pygame.mixer.Sound(file_path) 
            pygame_sound.play()
        
    
    def play(self, audio):

        check = True

        while check:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.play_audio(audio)

                    if event.key == pygame.K_0:
                        check = False
                        print("[red]Audio Canceled")

            pygame.display.update()


if __name__ == "__main__":
    # pygame.init()
    # screen = pygame.display.set_mode((800, 800))
    # radio = AudioManager()


    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
            
    #         if event.type == pygame.MOUSEBUTTONUP:
    #             radio.play_audio("audio_test.mp3")

    radio = AudioManager()
    radio.play("audio_test.mp3")
    pass