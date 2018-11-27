import pygame

(width, height) = (300, 200)
color=(10,10,10)
pos=(10,10)
screen = pygame.display.set_mode((width, height))
tf=True
while tf:	
	pygame.event.get()
	keys = pygame.key.get_pressed()
	if pygame.event.EventType == pygame.QUIT:
		tf = False
	pygame.draw.circle(screen,color,pos,5,0)
	pygame.display.flip()
	pygame.time.delay(500)


pygame.quit