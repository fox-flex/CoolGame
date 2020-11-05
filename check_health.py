import pygame
pygame.init()

loss_sound = pygame.mixer.Sound('audio/loss.wav')

def check_lives():
    """
    After mistake check, if user has enough lives to continue.
    """
    global lives
    lives -= 1
    if lives == 0:
        pygame.mixer.Sound.play(loss_sound)
        # in production:
        game_over()
        return False
    else:
        return True
