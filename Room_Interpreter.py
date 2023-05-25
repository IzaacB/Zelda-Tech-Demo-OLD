import pygame
import Room_Data

class Room:
    def __init__(self, x_origin, y_origin):
        self.x0 = x_origin
        self.y0 = y_origin
        self.tile_x = x_origin
        self.tile_y = y_origin
        self.wall_sprite = pygame.image.load('Sprites/Dungeon/Base_Wall.png')

    def read(self, room_data, window):
        #Initialize different tile layers.
        self.tiles_back = []
        self.tiles_mid = []
        self.tiles_front = []
        #Draw the wall outline for each room.
        self.tiles_front.append([self.wall_sprite, self.x0, self.y0])

        #Iterate through nested lists for room tiles.
        for i in range(len(room_data)):
            for j in range(len(room_data[i])):

                #Set floor tiles.
                if room_data[i][j] in Room_Data.floor_tiles:
                    if j <= 1 or j >= 14:
                        self.tiles_back.append([Room_Data.tile_sprites[room_data[i][j]], self.tile_x, self.tile_y + 8])
                    else:
                        self.tiles_back.append([Room_Data.tile_sprites[room_data[i][j]], self.tile_x, self.tile_y])

                #Set collision tiles.
                if room_data[i][j] in Room_Data.collision_tiles:
                    if j <= 1 or j >= 14:
                        self.tiles_mid.append([Room_Data.tile_sprites[room_data[i][j]], self.tile_x, self.tile_y + 8])
                    else:
                        self.tiles_mid.append([Room_Data.tile_sprites[room_data[i][j]], self.tile_x, self.tile_y])

                #Set wall/ceiling tiles.
                if room_data[i][j] in Room_Data.ceiling_tiles:
                    if j <= 1 or j >= 14:
                        self.tiles_front.append([Room_Data.tile_sprites[room_data[i][j]], self.tile_x, self.tile_y + 8])
                    else:
                        self.tiles_front.append([Room_Data.tile_sprites[room_data[i][j]], self.tile_x, self.tile_y])

                self.tile_x += 16

            #Set next tile location.
            self.tile_y += 16
            self.tile_x = self.x0

        #Reset y position each row.
        self.tile_y = self.y0

        #Return the tileset for Dungeon generation.
        return [self.tiles_back, self.tiles_mid, self.tiles_front]