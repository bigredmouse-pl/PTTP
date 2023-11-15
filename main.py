import pygame
import sys,random



def display_images():
    pygame.init()

    width, height = 1200, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wyświetlanie obrazków w Pygame")


    clock = pygame.time.Clock()
    value1= 0
    value2 =0


    def gauge( x,y,name,alt_value,value):
        step = 1
        if alt_value < value:
            step = 1
        if alt_value >value:
            step = -1
        font = pygame.font.Font(None, 36)
        bg_image = pygame.image.load("images/gauge_bg_240.png")
        for angle in range(alt_value,value,step):
            pointer_image = pygame.image.load("images/pointer_120.png")
            pointer_image = pygame.transform.rotate(pointer_image, int(135 - angle*2.7))
            bg_rect = bg_image.get_rect(center=(x,y))
            pointer_rect = pointer_image.get_rect(center=bg_rect.center)
            text_surface_1 = font.render(name, True, (160, 160, 160))
            text_surface_2 = font.render(str(value), True, (255, 255, 255))
            text_rect_1 = text_surface_1.get_rect(center=(x,  y -40))
            text_rect_2 = text_surface_2.get_rect(center=(x, y + 80))
            screen.blit(bg_image, bg_rect)
            screen.blit(text_surface_1, text_rect_1)
            screen.blit(pointer_image, pointer_rect)
            screen.blit(text_surface_2, text_rect_2)
            pygame.display.update(bg_rect)
            pygame.time.delay(10)

    def score_bar(score,size):
        bg_image = pygame.image.load("images/golden_line.png")
        sparkle_image = pygame.image.load("images/sparkle.png")
        sparkle_image.
        screen.blit(bg_image,(100,200))
        screen.blit(sparkle_image, (100+score*5, 300+score))


    alt_end1 = 0
    alt_end2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #screen.fill((255, 255, 255))  # Białe tło
        bg = pygame.image.load("images/gamepad_screen.jpg")
        d1 = pygame.image.load("images/line-clipart-L.png")
        screen.blit(bg, (0,0))
        score_bar(random.randint(1,100),40)
        end1 = random.randint(1,100)
        end2 = random.randint(1, 100)

        gauge(150,150,"attention",alt_end1,end1)
        gauge(150, 650, "meditation",alt_end2,end2)

        alt_end1 = end1
        alt_end2 = end2




        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    display_images()
