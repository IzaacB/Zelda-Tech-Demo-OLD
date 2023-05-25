import pygame
import Room_Interpreter
import Room_Data

class Map:
    def __init__(self, x_origin, y_origin):
        self.x0 = x_origin
        self.y0 = y_origin
        self.room_x = x_origin
        self.room_y = y_origin
        self.wall_sprite = pygame.image.load('Sprites/Dungeon/Base_Wall.png')

    def update(self, x, y):
        self.x0 = x
        self.y0 = y
        self.room_x = x
        self.room_y = y
    def read(self, map_data, window):
        #Initialze different tile layers.
        self.tiles_back = []
        self.tiles_mid = []
        self.tiles_front = []

        for i in range(len(map_data)):
            for j in range(len(map_data[i])):
                if map_data[i][j] != 0:
                    #Inherit tile layers from each room in Map_Data.
                    self.room = Room_Interpreter.Room(self.room_x, self.room_y)
                    self.tiles = self.room.read(Room_Data.room_layout[map_data[i][j]], window)
                    self.tiles_back += self.tiles[0]
                    self.tiles_mid += self.tiles[1]
                    self.tiles_front += self.tiles[2]
                    self.tiles_front.append([self.wall_sprite, self.room_x, self.room_y])

                #Set next room location
                self.room_x += 256

            self.room_y += 176
            self.room_x = self.x0

        self.room_y = self.y0

        #Return the different tile layers.
        return [self.tiles_back, self.tiles_mid, self.tiles_front]