import pygame
import time
#Funktion til at sættte variabler til "" eller 0
def var():
    global a,b,c,d,s1,s2,s3,s4,h,q,o,svar
    #Svar mugligheder
    a = ""
    b = ""
    c = ""
    d = ""
    #Tal til spørgsmåæ
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    #Overskrift
    h = ""
    #spørgsmål
    q = ""
    #Opgave oppe i venstre hjørne
    o = ""
    #Hvilket svar man har valgt
    svar = 0
#Her sætter vi tallene foran spørgsmålene
def s():
    global s1,s2,s3,s4
    s1 = "1."
    s2 = "2."
    s3 = "3."
    s4 = "4."
#Her starter vi vores program.
def main():
    global a,b,c,d,s1,s2,s3,s4,h,q,o,svar
    #Sætte variabler op til senere.
    var()
    #tf til at starte loopet tf : True/False
    tf = True
    intro = False
    #korrekt svar
    ksvar = False
    #Bogstaver der bliver trykket
    counter = 0
    char = "1"
    #Variabler til opgaver
    o_start = False
    o_1 = False
    o_2 = False
    stop = False
    
    #Intro
    h = "Velkommen til vores spil"
    q = "Tryk mellemrum for at forsætte"
    #start Pygame
    pygame.init()
    #Title på Pygame display
    pygame.display.set_caption('Et lære spil')
    #Skærm
    surface_sz = 600  
    main_surface = pygame.display.set_mode((surface_sz*2, surface_sz))
    
    #Fonte til at bruge senere 20,26... er skrift størrelse
    font_1 = pygame.font.SysFont("Calibri", 20)
    font_2 = pygame.font.SysFont("Calibri", 26)
    font_3 = pygame.font.SysFont("Calibri", 30)
    font_4 = pygame.font.SysFont("Calibri", 40)
    font_5 = pygame.font.SysFont("Calibri", 50)

    #Frame til at se programmet køre
    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()
    
    while tf:
        #Text. Intro, overskrift. Her sætter vi vores variabler h,q,o til at være text, (0,0,0) er farve går til 255, True for at teksten ikke bliver pixelerede. 
        text_hilsen = font_5.render( h , True, (0,0,0))
        text_q = font_3.render( q , True, (0,0,0))
        text_opgave = font_2.render( o , True, (0,0,0))
        
        #Text. Spørgsmål. variabler a,b,c,d
        text_a = font_2.render(a, True, (0,0,0))
        text_b = font_2.render(b, True, (0,0,0))
        text_c = font_2.render(c, True, (0,0,0))
        text_d = font_2.render(d, True, (0,0,0))
        
        #Tal. Spørgsmål. Variabler s1,s2,s3,s4
        text_s1 = font_3.render(s1, True, (0,0,0))
        text_s2 = font_3.render(s2, True, (0,0,0))
        text_s3 = font_3.render(s3, True, (0,0,0))
        text_s4 = font_3.render(s4, True, (0,0,0))
        
        #Framerate. Text. Variabler frame_count, frame_rate
        text_fr = font_1.render("Frame rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))

        #Længde. spørgsmål. Variabler, a,b,c,d og aL,bL,cL,dL.
        #Her finder vi længden af vores spørgsmål. Ikke hvor mange bogstaver der er i dem. divider med 2 for at vi kan sætte spørgsmålet i midten.
        aL = text_a.get_rect().width/2
        bL = text_b.get_rect().width/2
        cL = text_c.get_rect().width/2
        dL = text_d.get_rect().width/2
        
        #Længde. Spørgsmål. Variabler, hilsen, q.
        hL = text_hilsen.get_rect().width/2
        qL = text_q.get_rect().width/2

        #Farve på baggrund
        main_surface.fill((0, 200, 255))
        #Tæl frames
        frame_count += 1

        #Framerate indlæses på surface
        main_surface.blit(text_fr, (surface_sz*2-210, 10))
        
        #Text variabler indlæses
        main_surface.blit(text_hilsen, ((surface_sz)-hL, 20))
        main_surface.blit(text_opgave, (10, 10))
        
        #Spørgsmål indlæses
        main_surface.blit(text_q, ((surface_sz-qL), (surface_sz/5)))
        
        #Tal. Spørgsmål 
        main_surface.blit(text_s1, ((surface_sz-qL), (surface_sz/5+50)))
        main_surface.blit(text_s2, ((surface_sz-qL), (surface_sz/5+100)))
        main_surface.blit(text_s3, ((surface_sz-qL), (surface_sz/5+150)))
        main_surface.blit(text_s4, ((surface_sz-qL), (surface_sz/5+200)))
        
        #Text. Spørgsmål
        main_surface.blit(text_a, ((surface_sz)-aL, (surface_sz/5+50)))
        main_surface.blit(text_b, ((surface_sz)-bL, (surface_sz/5+100)))
        main_surface.blit(text_c, ((surface_sz)-cL, (surface_sz/5+150)))
        main_surface.blit(text_d, ((surface_sz)-dL, (surface_sz/5+200)))
        
        #Nu har vi sat en framerate op så vi kan se spillet køre
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        #Check om spørgsmål 1 er svaret rigtigt
        if o_1 == True and o_2 == False:
            #Hvis svaret er rigtigt
            if svar == 1:
                var()
                svar = 0
                #ksvar er om det rigtige svar er fundet.
                ksvar = True
                q = "Du valgte det korrekte svar"
                a = "a = 10"
                b = "Dette ville definere a som 10"
                c = "Mellemrum for at fortsætte"
            #Hvis svaret er forkert
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
                
        #Check om spørgsmål 2 er svaret rigtigt
        if o_2 == True:
            if svar == 1:
                var()
                q = "Du valgte det forkerte svar"
                a = "b = false"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
            elif svar == 2:
                var()
                q = "Du valgte det forkerte svar"
                a = "b = false"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
            #Hvis svaret er rigtigt
            elif svar == 3:
                var()
                ksvar = True
                stop = True
                svar = 0
                q = "Du valgte det rigtige svar"
                a = "b = False"
                b = "Dette vil sætte b til at være variablen False"
                c = "Mellemrum for at forsætte"
                stop = True
            elif svar == 4:
                var()
                q = "Du valgte det forkerte svar"
                a = "b = 0"
                b = "Dette vil sætte b til at være variablen false"
                c = "Mellemrum for at forsætte"
                
        #Et for loop der køre hvis man bevæger musen over vinduet eller trykker på en knap 
        for event in pygame.event.get():
            #Her sætter vi en variabel der husker hvad der bliver trykket
            keys = pygame.key.get_pressed()
            
            if not event.type == pygame.MOUSEMOTION:
                
            if counter/2 == 1:
                    if keys[pygame.K_a]:
                        char = "a"
                        counter = 0
                    if keys[pygame.K_b]:
                        char = "b"
                    if keys[pygame.K_c]:
                        char = "c"
                    if keys[pygame.K_d]:
                        char = "d"
                    if keys[pygame.K_e]:
                        char = "e"
                    if keys[pygame.K_f]:
                        char = "f"
                    if keys[pygame.K_g]:
                        char = "g"
                    if keys[pygame.K_h]:
                        char = "h"
                    if keys[pygame.K_i]:
                        char = "i"
                    if keys[pygame.K_j]:
                        char = "j"
                    if keys[pygame.K_k]:
                        char = "k"
                    if keys[pygame.K_l]:
                        char = "e"
                    if keys[pygame.K_m]:
                        char = "m"
                    if keys[pygame.K_n]:
                        char = "n"
                    if keys[pygame.K_o]:
                        char = "o"
                    if keys[pygame.K_p]:
                        char = "p"
                    if keys[pygame.K_q]:
                        char = "q"
                    if keys[pygame.K_r]:
                        char = "r"
                    if keys[pygame.K_s]:
                        char = "s"
                    if keys[pygame.K_t]:
                        char = "t"
                    if keys[pygame.K_u]:
                        char = "u"
                    if keys[pygame.K_v]:
                        char = "v"
                    if keys[pygame.K_w]:
                        char = "w"
                    if keys[pygame.K_x]:
                        char = "x"
                    if keys[pygame.K_y]:
                        char = "y"
                    if keys[pygame.K_z]:
                        char = "z"
            print(char)

            #Start 1. spørgsmål
            if keys[pygame.K_SPACE] and intro == True and ksvar == False and o_2 == False:
                o_1 = True
                start = True
                o = "Opgave 1"
                h = "Variabler"
                q = "Vores variabler a skal være en integer lig med 10. Hvordan gøres dette?"
                s()
                a = "a = 10"
                b = "int(a) = 10"
                c = "a int = 10"
                d = "a: 10"
            #Start 2. spørgsmål
            if keys[pygame.K_SPACE] and o_2 == True and ksvar == False or o_start == True:
                o_start = False
                o = "Opgave 2"
                h = "Boolean"
                q = "Variabel b skal være en boolean med en falsk værdi. Hvordan gøres dette?"
                s()
                a = "b = false"
                b = "b = true"
                c = "b = False"
                d = "b = 0"
            #Introduktionen
            if keys[pygame.K_SPACE] and intro == False:
                o = "Information"
                h = "Intro"
                a = "Vælg denne mulighed ved at trykke 1"
                b = "Vælg denne mulighed ved at trykke 2"
                c = "Vælg denne mulighed ved at trykke 3"
                d = "Vælg denne mulighed ved at trykke 4"
                start = False
                intro = True
            #Den skal kun se om man klikker på knapperne hvis det rigtige svar ikke er fundet
            if intro == True and start == True and ksvar == False and stop == False:
                #I if statements ser vi hvilken knap der er trykket og hvad den skal gøre ved den knap.
                if keys[pygame.K_1]:
                        svar = 1
                if keys[pygame.K_2]:
                        svar = 2
                if keys[pygame.K_3]:
                        svar = 3
                if keys[pygame.K_4]:
                        svar = 4
            #Fra opgave 1 til 2
            if ksvar == True and o_1 == True and stop == False:
                if keys[pygame.K_SPACE]:
                    var()
                    ksvar = False
                    o_start = True
                    o_2 = True
            #fra opgave 2 til 3
            if ksvar == True and o_2 == True and stop == False:
                if keys[pygame.K_SPACE] and o_2 == True:
                    var()
                    o_2 = True
                    ksvar = False
            #Her ser vi om man har svaret på alle opgaverne ved brug af booleanen stop
            if ksvar == True and keys[pygame.K_SPACE] and stop == True:
                var()
                o = "Slut"
                h = "Tillyke du er færdig med spillet"
            #Her finder vi om man lukker vinduet.
            if event.type == pygame.QUIT:
                #Den stopper while loopet.
                tf = False
        
        pygame.display.flip()

    pygame.quit()

main()
