from managers.openai_manager import OpenAIManager
import managers.speech_manager as sm
import managers.elevenlabs_manager as ele
from managers.audio_manager import AudioManager
import pygame
from rich import print


class Bot:
    def __init__(self, name, bio):
        self.name = name
        self.bot = OpenAIManager()
        self.bot.create_character(bio)

    def conversation(self):
        # gets the question you ask in speaker
        prompt = sm.recognize_from_microphone()
        # gets response from chatgpt
        answer = self.bot.chat_with_history(prompt)
        # turns response into audio
        audio = ele.text_to_speech_file(answer)

        return audio

    def display(self):
        pygame.init()
        pygame.display.set_caption("Chat Bot")
        
        background = pygame.image.load("spiderman.png")

        screen = pygame.display.set_mode((1000, 500))

        # initialize Audio Manager (one that plays the audio out loud)
        # audio can only play when pygame is being displayed
        radio = AudioManager()

        while True:
            screen.blit(background, (0, 0))
            # needed for pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        audio = self.conversation()
                        radio.play_audio(audio)

            pygame.display.update()


if __name__ == "__main__":

    miles_bio = """
        You are Miles Morales from Spiderman into the Spiderverse. You are really into music and you
        always mention your favorite artist, Post Malone. Mid response you start singing some of 
        your favorite Post Malone song, Sunflower.
        Ensure everybody that you are not spiderman. Anytime someone brings up that you
        are spiderman, you adamantly deny it. You say "Imma do my own thing" very frequently.
        You always try to compliment Spiderman all the time, but are still outwardly
        pretending you aren't Spiderman. Anytime you want to sing, say a long string of vowels, that are
        mostly a's and e's. For example say "aaa ayyyy aeeeuoaaueoe". 
        Real Madrid is your favorite soccer club.
        You are a diehard Real Madrid fan and you believe that they will win the Champions League
        You are also a diehard Barca hater and emphasize on that they will never win another Champions League again.

        """

    miles = Bot("Miles", miles_bio)
    miles.display()
