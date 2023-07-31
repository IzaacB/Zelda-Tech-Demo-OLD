import pygame

#The purpose of this script is to just store the specific room data by keying tiles and sending them to the room interpreter script.

room_layout = {
    1 : [[ 0, 0, 0, 0, 0, 0, 0,10,10, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [15,20, 1, 1,22,22, 1, 1, 1, 1,22,22, 1, 1, 7,12],
         [15,20, 1, 1,22,22, 1, 1, 1, 1,22,22, 1, 1, 6,12],
         [ 0, 0, 1, 1,22,22, 1, 1, 1, 1,22,22, 1, 1, 0, 0],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0,19,19, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0,0 ,17,17, 0, 0, 0, 0, 0, 0, 0]],

    2 : [[ 0, 0, 0, 0, 0, 0, 0,14,14, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0,18,18, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0,26,26,26,26,26, 1, 1,26,26,26,26,26, 0, 0],
         [ 0, 0,26,26,26,26,26, 1, 1,26,26,26,26,26, 0, 0],
         [15,20, 1, 1,26,26,26, 1, 1, 1, 1, 1, 1, 1, 7,12],
         [15,20, 1, 1,26,26,26, 1, 1, 1, 1, 1, 1, 1, 6,12],
         [ 0, 0, 1, 1,26,26,26, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0,26,26,26,26,26, 1, 1,26,26,26,26,26, 0, 0],
         [ 0, 0,26,26,26,26,26, 1, 1,26,26,26,26,26, 0, 0],
         [ 0, 0,26,26,26,26,26, 8, 9,26,26,26,26,26, 0, 0],
         [ 0, 0, 0, 0, 0, 0,0 ,13,13, 0, 0, 0, 0, 0, 0, 0]],

    3 : [[ 0, 0, 0, 0, 0, 0, 0,14,14, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0,18,18, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0, 1,23, 1, 1, 1, 1, 1, 1, 1, 1,24, 1, 0, 0],
         [11, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 21,16],
         [11, 4, 1, 1, 1,23, 1, 1, 1, 1, 24, 1, 1, 1, 21,16],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0, 1,23, 1, 1, 1, 1, 1, 1, 1, 1,24, 1, 0, 0],
         [ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 8, 9, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0,0 ,13,13, 0, 0, 0, 0, 0, 0, 0]],

    4 : [[ 0, 0, 0, 0, 0, 0, 0,10,10, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0,25,25,25,25,25,25,25,25,25,25,25,25, 0, 0],
         [ 0, 0,25,25,25,25,25,25,25,25,25,25,25,25, 0, 0],
         [11, 5,25,25,25,25,25,25,25,25,25,25,25,25,21,16],
         [11, 4,25,25,25,25,25,25,25,25,25,25,25,25,21,16],
         [ 0, 0,25,25,25,25,25,25,25,25,25,25,25,25, 0, 0],
         [ 0, 0,25,25,25,25,25,25,25,25,25,25,25,25, 0, 0],
         [ 0, 0,25,25,25,25,25,25,25,25,25,25,25,25, 0, 0],
         [ 0, 0, 0, 0, 0, 0, 0,19,19, 0, 0, 0, 0, 0, 0, 0],
         [ 0, 0, 0, 0, 0, 0,0 ,17,17, 0, 0, 0, 0, 0, 0, 0]],
}

tile_sprites = {
     0:  pygame.image.load('Sprites/Dungeon/Tiles/Tile5.png'),   #   Black collision tile.
     1:  pygame.image.load('Sprites/Dungeon/Tiles/Tile1.png'),   #   Base floor tile.
     2:  pygame.image.load('Sprites/Dungeon/Tiles/Tile11.png'),  #   Top/Right door under.
     3:  pygame.image.load('Sprites/Dungeon/Tiles/Tile12.png'),  #   Top/Left door under.
     4:  pygame.image.load('Sprites/Dungeon/Tiles/Tile13.png'),  #   Left/Bottom door under.
     5:  pygame.image.load('Sprites/Dungeon/Tiles/Tile14.png'),  #   Left/Top door under.
     6:  pygame.image.load('Sprites/Dungeon/Tiles/Tile15.png'),  #   Right/Bottom door under.
     7:  pygame.image.load('Sprites/Dungeon/Tiles/Tile16.png'),  #   Right/Top door under.
     8:  pygame.image.load('Sprites/Dungeon/Tiles/Tile17.png'),  #   Bottom/Left door under.
     9:  pygame.image.load('Sprites/Dungeon/Tiles/Tile18.png'),  #   Bottom/Right door under.
     10: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead1.png'),    #    Door overhead open top.
     11: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead2.png'),    #    Door overhead open left.
     12: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead3.png'),    #    Door overhead open right.
     13: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead4.png'),    #    Door overhead open bottom.
     14: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead5.png'),    #    Door overhead closed top.
     15: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead6.png'),    #    Door overhead closed left.
     16: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead7.png'),    #    Door overhead closed right.
     17: pygame.image.load('Sprites/Dungeon/Tiles/Door_Overhead8.png'),    #    Door overhead closed bottom.
     18:  pygame.image.load('Sprites/Dungeon/Tiles/Tile19.png'),  #   Top door closed under.
     19:  pygame.image.load('Sprites/Dungeon/Tiles/Tile22.png'),  #   Bottom door closed under.
     20:  pygame.image.load('Sprites/Dungeon/Tiles/Tile20.png'),  #   Left closed door under.
     21:  pygame.image.load('Sprites/Dungeon/Tiles/Tile21.png'),  #   Right closed door under.
     22: pygame.image.load('Sprites/Dungeon/Tiles/Tile2.png'),    #   Block tile.
     23: pygame.image.load('Sprites/Dungeon/Tiles/Tile3.png'),    #   Weird fish statue.
     24: pygame.image.load('Sprites/Dungeon/Tiles/Tile4.png'),    #   Another weird fish statue.
     25: pygame.image.load('Sprites/Dungeon/Tiles/Tile6.png'),    #   Sand floor tile.
     26: pygame.image.load('Sprites/Dungeon/Tiles/Tile27.png')    #   Water tile.
}

#Organize the tiles into these lists so the interepreter knows what tiles to draw in order, and what also collides with the player.
floor_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 25]
collision_tiles = [0, 18, 19, 20, 21, 22, 23, 24, 26]
ceiling_tiles = [10, 11, 12, 13, 14, 15, 16, 17]
