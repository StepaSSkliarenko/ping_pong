import pygame
pygame.font.init()



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width,player_height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < h - 100:
            self.rect.y += self.speed

    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < h - 100:
            self.rect.y += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, player_width,player_height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= h - 50:
            self.speed_y *= -1
        if pygame.sprite.collide_rect(rocet_l, ball) or pygame.sprite.collide_rect(rocet_r, ball):
            self.speed_x *= -1

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
            
w = 1280
h = 720
font = pygame.font.SysFont("Arial", 60)
win = font.render("Победа игрока с лева", True, (0, 0, 0))
lose = font.render("Победа игрока с права", True, (0, 0, 0))
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
rocet_l = Player("r.png", 0, 0, 10, 25, 100)
rocet_r = Player("r.png", w-35, h -100, 10, 25, 100)
ball = Ball("b.png", w/2, h/2, 5, 5, 50, 50)
game = True
finish = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not finish:   
        window.fill((200, 255, 255))
        ball.reset()
        ball.update()
        rocet_l.reset()
        rocet_l.update_l()
        rocet_r.reset()
        rocet_r.update_r()
        if ball.rect.x == -50:
            window.blit(lose,(w//2, h//2))
            finish = True
        if ball.rect.x == w + 50:
            window.blit(win,(w//2, h//2))
            finish = True
        pygame.display.update()
        clock.tick(60)





