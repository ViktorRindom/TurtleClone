import pygame
import time


def main():
    tf = True
    pygame.init()
    pygame.display.set_caption('Et lære spil')
    
    surface_sz = 720   
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    
    font_1 = pygame.font.SysFont("Calibri", 16)
    font_2 = pygame.font.SysFont("Calibri", 26)
    
    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()
    
    #Text
    text_opgave = font_2.render("Opgave 1", True, (0,0,0))
    text_hilsen = font_2.render("Velkommen til vores spil", True, (0,0,0))
    text_1 = font_1.render("", True, (0,0,0))


    while tf:
        #Farve på baggrund
        main_surface.fill((0, 200, 255))
        
        #Frames
        frame_count += 1
        #Framerate Text
        text_fr = font_1.render("Frame rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))

        #Framerate indlæses på surface
        main_surface.blit(text_fr, (surface_sz - 160, 10))
        #Text variabler indlæses
        main_surface.blit(text_hilsen, (surface_sz/2, surface_sz/2))
        main_surface.blit(text_opgave, (10, 10))
        main_surface.blit(text_1, (surface_sz/2, surface_sz/2))
        
        #Nu har vi sat en framerate op så vi kan se spillet køre
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1-t0)
            t0 = t1
  
                
        #Et for loop der køre hvis man bevæger musen over vinduet eller trykker på en knap
        for event in pygame.event.get():
            #Her sætter vi en variabel der husker hvad der bliver trykket
            keys = pygame.key.get_pressed()
            
            #I if statements ser vi hvilken knap der er trykket og hvad den skal gøre ved den knap.
            if keys[pygame.K_LEFT]:
                    print("Left")
                    text_1 = font_1.render("Forkert svar", True, (0,0,0))
                    text_hilsen = font_2.render("", True, (0,0,0))
            if keys[pygame.K_RIGHT]:
                    print("Right")
                    text_1 = font_1.render("Rigtigt", True, (0,0,0))
                    text_hilsen = font_2.render("", True, (0,0,0))
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
