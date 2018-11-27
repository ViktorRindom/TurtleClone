import pygame
import time
tf = True


def main():
    global tf
    pygame.init()
    pygame.display.set_caption('Et lære spil')
    surface_sz = 480   
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    font_1 = pygame.font.SysFont("Courier", 16)
    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()

    while tf:
        main_surface.fill((0, 200, 255))
        frame_count += 1
        text = font_1.render("Frame = {0}, rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))
        main_surface.blit(text, (10, 10))
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1-t0)
            t0 = t1
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                print("Left")
            if keys[pygame.K_RIGHT]:
                print("Right")
            if keys[pygame.K_UP]:
                print("Up")
            if keys[pygame.K_DOWN]:
                print("Down")
            if event.type == pygame.QUIT: 
                tf = False
            
        pygame.display.flip()

    pygame.quit()

main()
