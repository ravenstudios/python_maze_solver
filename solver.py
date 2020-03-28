from constants import *
import pygame
import math

class Solver:
    def __init__(self):
        self.places = self.solve(MAZE_TILES)
        print(self.places)

    def update(self):
        pass


    def draw(self, surface):
        for place in self.places:
            x = place % 8 * BLOCK_SIZE
            y = place // 8 * BLOCK_SIZE
            pygame.draw.rect(surface, (255, 0, 255), (x + BLOCK_SIZE / 4, y + BLOCK_SIZE / 4, BLOCK_SIZE // 2, BLOCK_SIZE // 2))

# MAZE_TILES = [
#     0, 0, 0, 0, 0, 0, 0, 0,
#     0, 2, 1, 1, 1, 1, 1, 0,
#     0, 0, 0, 0, 1, 0, 0, 0,
#     0, 0, 0, 0, 1, 0, 1, 0,
#     0, 0, 1, 1, 1, 1, 1, 0,
#     0, 0, 0, 1, 0, 0, 1, 0,
#     0, 1, 1, 1, 1, 0, 0, 0,
#     0, 0, 0, 1, 1, 1, 3, 0
# ]



    def solve(self, arr):
        start_location = arr.index(2)#2 is the code for the start place in the array, this will change to a better var name
        mul = int(math.sqrt(len(MAZE_TILES)))

        rows = mul
        cols = mul

        visited_places = []

        open_places = []

        current_place = start_location

        while True:
            print(current_place)
            #up
            u_pos = current_place - mul
            if u_pos > -1 and u_pos < len(arr):
                if arr[u_pos] == 3:
                    print("end is at", u_pos)
                    visited_places.append(u_pos)
                    visited_places.append(current_place)
                    return visited_places

                if arr[u_pos] == 1 and not u_pos in visited_places:
                    open_places.append(u_pos)

            #right
            r_pos = current_place + 1
            if r_pos > -1 and r_pos < len(arr):
                if arr[r_pos] == 3:
                    print("end is at", r_pos)
                    visited_places.append(r_pos)
                    visited_places.append(current_place)
                    return visited_places

                if arr[r_pos] == 1 and not r_pos in visited_places:
                    open_places.append(r_pos)

            #down
            d_pos = current_place + mul
            if d_pos > -1 and d_pos < len(arr):
                if arr[d_pos] == 3:
                    print("end is at", d_pos)
                    visited_places.append(d_pos)
                    visited_places.append(current_place)
                    return visited_places

                if arr[d_pos] == 1 and not d_pos in visited_places:
                    open_places.append(d_pos)

            #left
            l_pos = current_place - 1
            if l_pos > -1 and l_pos < len(arr):
                if arr[l_pos] == 3:
                    print("end is at", l_pos)
                    visited_places.append(l_pos)
                    visited_places.append(current_place)
                    return visited_places

                if arr[l_pos] == 1 and not l_pos in visited_places:
                    open_places.append(l_pos)

            visited_places.append(current_place)
            current_place = open_places[0]
            open_places.pop(0)
