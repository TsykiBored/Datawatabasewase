import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([780, 750])
background_colour = (0, 0, 0)
pygame.display.set_caption('Student Data Wata')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

base_font = pygame.font.Font(None,25)

user_text = ""

text_surface = base_font.render(user_text, True, (255,255,255))

ID_rect = pygame.Rect(20,20,140,32)
FNAME_rect = pygame.Rect(20,20,140,32)
SNAME_rect = pygame.Rect(20,20,140,32)
AGE_rect = pygame.Rect(20,20,140,32)

run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
					if ID_rect.collidepoint(event.pos):
						IDactive = True
					else:
						IDactive = False
					if ID_rect.collidepoint(event.pos):
						FNAMEactive = True
					else:
						FNAMEactive = False
					if ID_rect.collidepoint(event.pos):
						SNAMEactive = True
					else:
						SNAMEacive = False	
					if ID_rect.collidepoint(event.pos):
						AGEactive = True
					else:
						AGEactive = False

	if event.type == pygame.KEYDOWN:
			if active == True:
				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				else:
					user_text += event.unicode

				if IDactive == True:
					ID = user_text
				elif FNAMEactive == True:
					FNAME = user_text
				elif SNAMEactive == True:
					SNAME = user_text
				elif AGEactive == True:
					AGE = user_text

screen.fill((255,255,255))


