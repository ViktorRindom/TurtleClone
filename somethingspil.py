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
        text_fr = font_1.render("Frame rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))
        text_1 = font_1.render("Velkommen til vores læringsspil", True, (0,0,0))
        main_surface.blit(text_fr, (10, 10))
        main_surface.blit(text_1, (10, 100))
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1-t0)
            t0 = t1
            
        #Et for loop der køre hvis man bevæger musen over vinduet eller trykker på en knap
        for event in pygame.event.get():
            #Her sætter vi en variabel til det der bliver trykket
            keys = pygame.key.get_pressed()

            #I if statements ser vi hvilken knap der er trykket og hvad den skal gøre ved den knap.
            if keys[pygame.K_LEFT]:
                print("Left")
                text_1 = text_1 = font_1.render("Left", True, (0,0,0))
                main_surface.blit(text_1, (10, 100))
            if keys[pygame.K_RIGHT]:
                print("Right")
            if keys[pygame.K_UP]:
                print("Up")
            if keys[pygame.K_DOWN]:
                print("Down")
            #Her finder vi om man lukker vinduet.
            if event.type == pygame.QUIT:
                #Den stopper while loopet.
                tf = False
            
        pygame.display.flip()

    pygame.quit()

main()
