import pygame.mixer


class SoundEffects:

    def play_alien_change_dir(self):
        pygame.mixer.music.load('alien_change_dir.mp3')
        pygame.mixer.music.play()

    def play_alien_hit(self):
        pygame.mixer.music.load('sounds/alien_hit.mp3')
        pygame.mixer.music.play()

    def play_shoot(self):
        pygame.mixer.music.load('sounds/shoot.mp3')
        pygame.mixer.music.play()