import pygame
import os

WIN = pygame.display.set_mode((900,500))
pygame.display.set_caption("p0")
FPS = 60
p1 = pygame.image.load(os.path.join('assests','ninja.png'))
P1 = pygame.transform.scale(p1,(100,90))
p2 = pygame.image.load(os.path.join('assests','turtle.png'))
P2 = pygame.transform.flip(pygame.transform.scale(p2,(100,90)),True,False)
velocity = 2
bullet_velocity = 10
middle_border = pygame.Rect(900/2-3,0,6,500)
bullets =[]
p1_score = 0



def p1_move(Keys_pressed,p1_rect,velocity):
    Keys_pressed = pygame.key.get_pressed()
    if Keys_pressed[pygame.K_LSHIFT]:
        velocity += 5
    if Keys_pressed[pygame.K_s] and p1_rect.y+90 + velocity <= 500:
        p1_rect.y += velocity
    if Keys_pressed[pygame.K_w] and p1_rect.y - velocity>0:
        p1_rect.y -= velocity
    if Keys_pressed[pygame.K_a] and p1_rect.x -velocity >0:
        p1_rect.x -= velocity
    if Keys_pressed[pygame.K_d] and p1_rect.x + 100 +velocity<= 445:
        p1_rect.x += velocity

def p2_move(Keys_pressed,p2_rect,velocity):
    
    if Keys_pressed[pygame.K_RSHIFT]:
        velocity += 5
    if Keys_pressed[pygame.K_DOWN]and p2_rect.y+90 + velocity <= 500:
        p2_rect.y += velocity
    if Keys_pressed[pygame.K_UP] and p2_rect.y - velocity>0:
        p2_rect.y -= velocity
    if Keys_pressed[pygame.K_LEFT] and p2_rect.x - velocity > 455:
        p2_rect.x -= velocity
    if Keys_pressed[pygame.K_RIGHT] and p2_rect.x + 100 + velocity < 900 :
        p2_rect.x += velocity

def draw(bullets,p1_rect,p2_rect):
    WIN.fill((255,255,255))
    pygame.draw.rect(WIN,(255,0,0),middle_border)
    for b in bullets:
        b.x += 10
        if b.x > 900 or p2_rect.colliderect(b):
            bullets.remove(b)
        else :
            pygame.draw.rect(WIN,(0,0,0),b)
    WIN.blit(P1,(p1_rect.x,p1_rect.y))
    WIN.blit(P2,(p2_rect.x,p2_rect.y))
    pygame.display.update()

def main():
    velocity = 2

    p1_rect = pygame.Rect(100,150,100,90)
    p2_rect = pygame.Rect(700,150,100,90)
    clock  = pygame.time.Clock()
    

    run =True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    buttlet = pygame.Rect(p1_rect.x+100,p1_rect.y+45,5,5)
                    bullets.append(buttlet)

        Keys_pressed = pygame.key.get_pressed()
        p1_move(Keys_pressed,p1_rect,velocity)
        p2_move(Keys_pressed,p2_rect,velocity)
        draw(bullets,p1_rect,p2_rect)
        
    pygame.quit()


if __name__ == "__main__":
    main()
