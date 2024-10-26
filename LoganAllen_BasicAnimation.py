
def main():
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Happy Birthday!")
    

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((69, 245, 210))
    
    frogBaby = pygame.image.load("frogBaby.png")
    frogBaby = frogBaby.convert_alpha()
    frogBaby = pygame.transform.scale(frogBaby, (640, 480))
    
    frogBaby_x = 0
    frogBaby_y = 0
    
    beardMan = pygame.image.load("beardMan.png")
    beardMan = beardMan.convert_alpha()
    beardMan = pygame.transform.scale(beardMan, (100, 100))
    
    beardMan_x = 0
    beardMan_y = 200
    
    beardMan2 = pygame.image.load("beardMan.png")
    beardMan2 = beardMan2.convert_alpha()
    beardMan2 = pygame.transform.scale(beardMan2, (100, 100))
    
    beardMan2_x = 540
    beardMan2_y = 200
    
    
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        beardMan_x += 3
        if beardMan_x > screen.get_width():
            beardMan_x = 0
                
        beardMan_y += 2
        if beardMan_y > screen.get_height():
            beardMan_y = 0
            
        beardMan2_y += 5
        if beardMan2_y > screen.get_height():
            beardMan2_y = 0
        
        beardMan2_x += 7
        if beardMan2_x > screen.get_width():
            beardMan2_x = 20
        
        screen.blit(background, (0, 0))
        screen.blit(frogBaby, (frogBaby_x, frogBaby_y))
        screen.blit(beardMan, (beardMan_x, beardMan_y))
        screen.blit(beardMan2, (beardMan2_x, beardMan2_y))
        pygame.display.flip()
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()