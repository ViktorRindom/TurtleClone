import pygame
tf = True

def main():
    global tf
    pygame.init()     
    surface_sz = 480   
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    while tf:
        main_surface.fill((0, 200, 255))
        for event in pygame.event.get():
            keys = pygame.get.key_pressed
            if keys[pygame.W]:
                print("w")
            if event.type == pygame.QUIT: 
                tf = False
                    
        pygame.display.flip()

    pygame.quit()
    

main()
