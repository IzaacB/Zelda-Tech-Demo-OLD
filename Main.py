import pygame
import Map_Data
import Map_Interpreter
import Player
pygame.init()

#Set up base colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
hud = pygame.image.load('Sprites/HUD/HUD_Bar.png')

#Initialize display.
window = pygame.display.set_mode((256, 224),pygame.SCALED, vsync=1)
refresh, refresh_rate = pygame.time.Clock(), 60

#Initialize gameobjects.
camera_x = 0
camera_y = -48
camera_x1 = camera_x
camera_y1 = camera_y
camera_speed = 240
camera_lock = 60

player = Player.Player(120, 128)
dungeon = Map_Interpreter.Map(-camera_x - 256 * 2, -camera_y - 176 * 5)

#Start main loop.
running = True
while running:

    #Measure frames in delta time.
    delta_time = refresh.tick(refresh_rate)/1000

    #Event handler for input.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Key press event handler.
    keys = pygame.key.get_pressed()

    #Update game objects.
    dungeon.update(-camera_x - 256 * 2, -camera_y - 176 * 5)
    tiles = dungeon.read(Map_Data.map_layout[0], window)

    if camera_x == camera_x1 and camera_y == camera_y1:
        player.update(keys, delta_time)

    player.check_collision(tiles[1], delta_time)

    #Update camera position.
    if camera_x == camera_x1 and camera_y == camera_y1:
        if player.rect.x >= window.get_width() - 16 and player.vel_x >= 0:
            camera_x1 = camera_x + 256
            player.rect.left = window.get_width() + 16

        if player.rect.x <= 0 and player.vel_x <= 0:
            camera_x1 = camera_x - 256
            player.rect.right = -16

        if player.rect.y >= window.get_height() and player.vel_y <= 0:
            camera_y1 = camera_y + 176
            player.rect.top = window.get_height() + 16

        if player.rect.y <= 0 + 48 and player.vel_y >= 0:
            camera_y1 = camera_y - 176
            player.rect.bottom = 32

    if camera_y > camera_y1:
        if camera_y <= camera_y1 + camera_speed/camera_lock:
            camera_y = camera_y1
            player.rect.y += camera_speed/camera_lock * delta_time

        else:
            camera_y -= camera_speed * delta_time
            player.rect.y += camera_speed * delta_time

    if camera_y < camera_y1:
        if camera_y >= camera_y1 - camera_speed/camera_lock:
            camera_y = camera_y1
            player.rect.y -= camera_speed/camera_lock * delta_time

        else:
            camera_y += camera_speed * delta_time
            player.rect.y -= camera_speed * delta_time

    if camera_x > camera_x1:
        if camera_x <= camera_x1 + camera_speed/camera_lock:
            camera_x = camera_x1
            player.rect.x += camera_speed/camera_lock * delta_time

        else:
            camera_x -= camera_speed * delta_time
            player.rect.x += camera_speed * delta_time

    if camera_x < camera_x1:
        if camera_x >= camera_x1 - camera_speed/camera_lock:
            camera_x = camera_x1
            player.rect.x -= camera_speed/camera_lock * delta_time

        else:
            camera_x += camera_speed * delta_time
            player.rect.x -= camera_speed * delta_time

    #Initalize render layers.
    render_layer_1 = []
    render_layer_2 = []
    render_layer_3 = []
    render_layer_4 = []
    final_render = []

    #Add game objects to render
    render_layer_2 += player.render(delta_time)
    render_layer_1 += tiles[0]
    render_layer_2 += tiles[1]
    render_layer_3 += tiles[2]
    render_layer_4 += [[hud, 0, 0]]


    #Finalize render.
    final_render += render_layer_1
    final_render += render_layer_2
    final_render += render_layer_3
    final_render += render_layer_4

    #Render out screen.
    window.fill(BLACK)

    for i in range(len(final_render)):
        if final_render[i][1] >= -256 and final_render[i][1] <= window.get_width() + 256 and final_render[i][2] >= -224 and final_render[i][2] <= window.get_height() + 224:
            window.blit(final_render[i][0], (final_render[i][1], final_render[i][2]))

    pygame.display.flip()

quit()