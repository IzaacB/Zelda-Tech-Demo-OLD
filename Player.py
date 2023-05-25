import pygame

class Player():
    def __init__(self, x, y):
        self.vel_x = 0
        self.vel_y = 0
        self.accel = 60
        self.friction = 60
        self.speed_cap = 60
        self.rect = pygame.Rect(x, y, 16, 16)

        self.sprite_dir = "DOWN"
        self.moving = False
        self.current_anim = 0
        self.frame = 0
        self.frames = {
            0: pygame.image.load('Sprites/Link/Link1.png'),#Down walk 1.
            1: pygame.image.load('Sprites/Link/Link2.png'),#Down walk 2.
            2: pygame.image.load('Sprites/Link/Link3.png'),#Right walk 1.
            3: pygame.image.load('Sprites/Link/Link4.png'),#Right walk 2.
            4: pygame.image.load('Sprites/Link/Link5.png'),#Up walk 1.
            5: pygame.image.load('Sprites/Link/Link6.png'),#Up walk 2.
            6: pygame.image.load('Sprites/Link/Link7.png'),#Left walk 1.
            7: pygame.image.load('Sprites/Link/Link8.png')#Left walk 2.
        }
        self.animations = {
            0: [self.frames[0], self.frames[1]],#Down walking.
            1: [self.frames[2], self.frames[3]],#Right walking.
            2: [self.frames[4], self.frames[5]],#Up walking.
            3: [self.frames[6], self.frames[7]]#Left walking
        }
    def update(self, keys, delta_time):
        if self.vel_x == 0:

            if keys[pygame.K_w] and self.vel_y <= self.speed_cap:
                self.vel_y += self.accel

            elif keys[pygame.K_s] and self.vel_y >= -self.speed_cap:
                self.vel_y -= self.accel

            else:
                if self.vel_y > 0:
                    if self.vel_y <= self.friction:
                        self.vel_y = 0

                    else:
                        self.vel_y -= self.friction

                elif self.vel_y < 0:
                    if self.vel_y >= self.friction:
                        self.vel_y = 0

                    else:
                        self.vel_y += self.friction

        if self.vel_y == 0:

            if keys[pygame.K_d] and self.vel_x <= self.speed_cap:
                self.vel_x += self.accel

            elif keys[pygame.K_a] and self.vel_x >= -self.speed_cap:
                self.vel_x -= self.accel

            else:
                if self.vel_x > 0:
                    if self.vel_x <= self.friction:
                        self.vel_x = 0

                    else:
                        self.vel_x -= self.friction

                elif self.vel_x < 0:
                    if self.vel_x >= self.friction:
                        self.vel_x = 0

                    else:
                        self.vel_x += self.friction

        self.rect.x += self.vel_x * delta_time
        self.rect.y -= self.vel_y * delta_time

    def check_collision(self, tiles, delta_time):
        for i in range(len(tiles)):
            self.tile_rect = pygame.Rect(tiles[i][1], tiles[i][2], 16, 16)
            self.colliding = self.rect.colliderect(self.tile_rect)
            if self.colliding:
                if self.vel_y < 0:
                    self.rect.bottom = self.tile_rect.top
                    self.vel_y = 0
                if self.vel_y > 0:
                    self.rect.top = self.tile_rect.bottom
                    self.vel_y = 0
                if self.vel_x < 0:
                    self.rect.left = self.tile_rect.right
                    self.vel_x = 0
                if self.vel_x > 0:
                    self.rect.right = self.tile_rect.left
                    self.vel_x = 0

    def render(self, delta_time):
        if self.vel_x > 0:
            self.sprite_dir == "RIGHT"
            self.moving = True
            self.current_anim = 1

        elif self.vel_x < 0:
            self.sprite_dir == "LEFT"
            self.moving = True
            self.current_anim = 3

        elif self.vel_y > 0:
            self.sprite_dir == "DOWN"
            self.moving = True
            self.current_anim = 2

        elif self.vel_y < 0:
            self.sprite_dir == "UP"
            self.moving = True
            self.current_anim = 0

        else:
            self.moving = False

        if self.moving == True:
            if self.frame < len(self.animations[self.current_anim]) - 1:
                self.frame += 5 * delta_time
                self.sprite = self.animations[self.current_anim][round(self.frame)]

            else:
                self.frame = 0
                self.sprite = self.animations[self.current_anim][round(self.frame)]
        else:
            self.sprite = self.animations[self.current_anim][round(self.frame)]

        return [[self.sprite,self.rect.x,self.rect.y]]