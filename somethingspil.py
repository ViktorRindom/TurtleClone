import pygame
import time

def var():
    global a,b,c,d,s1,s2,s3,s4,h,q,o,svar
    a = ""
    b = ""
    c = ""
    d = ""
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    h = ""
    q = ""
    o = ""
    svar = 0
def s():
    global s1,s2,s3,s4
    s1 = "1."
    s2 = "2."
    s3 = "3."
    s4 = "4."

def main():
    global a,b,c,d,s1,s2,s3,s4,h,q,o,svar
    var()
    svar = 0
    tf = True
    intro = False
    ksvar = False
    o_1 = False
    o_2 = False
    h = "Velkommen til vores spil"
    q = "Tryk mellemrum for at forsætte"
    
    pygame.init()
    pygame.display.set_caption('Et lære spil')
    
    surface_sz = 600   
    main_surface = pygame.display.set_mode((surface_sz*2, surface_sz))

    font_1 = pygame.font.SysFont("Calibri", 20)
    font_2 = pygame.font.SysFont("Calibri", 26)
    font_3 = pygame.font.SysFont("Calibri", 30)
    font_4 = pygame.font.SysFont("Calibri", 40)
    font_5 = pygame.font.SysFont("Calibri", 50)

    
    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()
    
    while tf:
        #Text
        text_hilsen = font_5.render(h, True, (0,0,0))
        text_q = font_3.render(q, True, (0,0,0))
        text_opgave = font_2.render(o, True, (0,0,0))
        
        text_a = font_2.render(a, True, (0,0,0))
        text_b = font_2.render(b, True, (0,0,0))
        text_c = font_2.render(c, True, (0,0,0))
        text_d = font_2.render(d, True, (0,0,0))

        text_s1 = font_3.render(s1, True, (0,0,0))
        text_s2 = font_3.render(s2, True, (0,0,0))
        text_s3 = font_3.render(s3, True, (0,0,0))
        text_s4 = font_3.render(s4, True, (0,0,0))
        

        aL = text_a.get_rect().width/2
        bL = text_b.get_rect().width/2
        cL = text_c.get_rect().width/2
        dL = text_d.get_rect().width/2
        
        hL = text_hilsen.get_rect().width/2
        qL = text_q.get_rect().width/2

        #Farve på baggrund
        main_surface.fill((0, 200, 255))
        #Frames
        frame_count += 1
        #Framerate Text
        text_fr = font_1.render("Frame rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))

        #Framerate indlæses på surface
        main_surface.blit(text_fr, (surface_sz*2 - 210, 10))
        #Text variabler indlæses
        main_surface.blit(text_hilsen, ((surface_sz)-hL, 20))
        main_surface.blit(text_opgave, (10, 10))
        
        main_surface.blit(text_q, ((surface_sz-qL), (surface_sz/5)))
        
        main_surface.blit(text_s1, ((surface_sz-qL), (surface_sz/5+50)))
        main_surface.blit(text_s2, ((surface_sz-qL), (surface_sz/5+100)))
        main_surface.blit(text_s3, ((surface_sz-qL), (surface_sz/5+150)))
        main_surface.blit(text_s4, ((surface_sz-qL), (surface_sz/5+200)))

        main_surface.blit(text_a, ((surface_sz)-aL, (surface_sz/5+50)))
        main_surface.blit(text_b, ((surface_sz)-bL, (surface_sz/5+100)))
        main_surface.blit(text_c, ((surface_sz)-cL, (surface_sz/5+150)))
        main_surface.blit(text_d, ((surface_sz)-dL, (surface_sz/5+200)))
        
        #Nu har vi sat en framerate op så vi kan se spillet køre
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1-t0)
            t0 = t1
            
        if o_1 == True:
            if svar == 1:
                var()
                svar = 0
                ksvar = True
                q = "Du valgte det korrekte svar"
                a = "a = 10"
                b = "Dette ville definere a som 10"
                c = "Mellemrum for at fortsætte"
            elif svar == 2:
                var()
                q = "Du valgte det forkerte svar"
                a = "int(a) = 10"
                b = "Dette ville give dig en syntax error"
                c = "Mellemrum for at fortsætte"
            elif svar == 3:
                var()
                q = "Du valgte det forkerte svar"
                a = "a int = 10"
                b = "Dette ville give dig en syntax error"
                c = "Mellemrum for at fortsætte"
            elif svar == 4:
                var()
                q = "Du valgte det forkerte svar"
                a = "a: 10"
                b = "Dette vil ikke definere a som 10"
                c = "Mellemrum for at fortsætte"
        if o_2 == True:
            if svar == 1:
                var()
                svar = 0
                q = "Du valgte det forkerte svar"
                a = "b = false"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
            elif svar == 2:
                var()
                svar = 0
                q = "Du valgte det forkerte svar"
                a = "b = false"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
            elif svar == 3:
                var()
                svar = 0
                q = "Du valgte det forkerte svar"
                a = "b = false"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
            elif svar == 4:
                var()
                svar = 0
                q = "Du valgte det forkerte svar"
                a = "b = false"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
        #Et for loop der køre hvis man bevæger musen over vinduet eller trykker på en knap 
        for event in pygame.event.get():
            #Her sætter vi en variabel der husker hvad der bliver trykket
            keys = pygame.key.get_pressed()
                
            if keys[pygame.K_SPACE] and intro == True and ksvar == False and o_2 == False:
                o_1 = True
                o = "Opgave 1"
                h = "Variabler"
                q = "Vores variabler a skal være en integer lig med 10. Hvordan gøres dette?"
                s()
                a = "a = 10"
                b = "int(a) = 10"
                c = "a int = 10"
                d = "a: 10"
            if keys[pygame.K_SPACE] and o_2 == True and ksvar == False:  
                o = "Opgave 2"
                h = "Boolean"
                q = "Variabel b skal være en boolean med en falsk værdi. Hvordan gøres dette?"
                s()
                a = "b = false"
                b = "b = true"
                c = "b = False"
                d = "b = 0"
            if keys[pygame.K_SPACE] and intro == False:
                o = "Information"
                h = "Intro"

                a = "Vælg denne mulighed ved at trykke 1"
                b = "Vælg denne mulighed ved at trykke 2"
                c = "Vælg denne mulighed ved at trykke 3"
                d = "Vælg denne mulighed ved at trykke 4"
                
                intro = True
                

            if intro == True and ksvar == False:
                #I if statements ser vi hvilken knap der er trykket og hvad den skal gøre ved den knap.
                if keys[pygame.K_1]:
                        svar = 1
                if keys[pygame.K_2]:
                        svar = 2
                if keys[pygame.K_3]:
                        svar = 3
                if keys[pygame.K_4]:
                        svar = 4
                        
            if ksvar == True and o_1 == True:
                if keys[pygame.K_SPACE]:
                    var()
                    ksvar = False
                    o_1 = False
                    o_2 = True
            if ksvar == True and o_2 == True:
                if keys[pygame.K_SPACE] and o_2 == True:
                    var()
                    ksvar = False
            #Her finder vi om man lukker vinduet.
            if event.type == pygame.QUIT:
                    #Den stopper while loopet.
                tf = False
        
        pygame.display.flip()

    pygame.quit()

main()
